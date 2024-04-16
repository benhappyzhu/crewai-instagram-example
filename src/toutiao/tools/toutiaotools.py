import requests
import json
import os

from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader

class ToutiaoTools:
  
  @tool('search toutiao')
  def search_toutiao(query: str) -> str:
    """
    使用此工具在今日头条上搜索信息。该工具返回今日头条搜索引擎的5个结果。
    """
    return ToutiaoTools.search(query)
  
  @tool('search toutiao user')
  def search_toutiao_user(query: str) -> str:
    """
    使用此工具在今日头条上搜索用户。该工具返回5个相关用户页面的结果。  
    """
    return ToutiaoTools.search(f"site:toutiao.com/user {query}", limit=5)
    
  @tool('open toutiao page')
  def open_toutiao_page(url: str) -> str:
    """
    使用此工具打开今日头条网页并获取内容。
    """
    loader = WebBaseLoader(url)    
    return loader.load()

  @tool('open page')
  def open_page(url: str) -> str:
    """
    Use this tool to open a webpage and get the content.
    """
    loader = WebBaseLoader(url)    
    return loader.load()    


  def search(query, limit=5):
    url = "https://www.toutiao.com/api/search/content/"
    payload = {
      "keyword": query, 
      "count": limit,
      "format": "json"
    }
    
    response = requests.get(url, params=payload) 
    results = response.json()['data']
    
    string = []
    for result in results:
      string.append(f"{result['title']}\n{result['abstract']}\n{result['article_url']}\n\n")
      
    return "".join(string)
