import requests
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

#search_string='nokia'


def obtain_product_reviews(search_string):
    search_url = f"https://www.flipkart.com/search?q={search_string}"
    uclient = ureq(search_url)  # getting response from the flipkart page
    all_prod_pg_source = uclient.read()#reading the webpage
    uclient.close()#closing server connection
    all_product_page_html = soup(all_prod_pg_source, 'html.parser')#html :source code
    bigboxes=all_product_page_html.findAll('div',{"class":"bhgxx2 col-12-12"})
    product_links=list()
    all_reviews=[]
    for box in bigboxes[2:-4]:
        links="https://www.flipkart.com"+box.div.div.div.a['href']
        product_links.append(links)
    #obtaining the reviews
    for link in product_links:
        review_page=requests.get(link)
        review_page_html=soup(review_page.text,'html.parser')
        review_boxes=review_page_html.find_all('div',{'class':'_3nrCtb'})
        for comment_box in review_boxes:
            try:
                comment_heading=comment_box.div.div.div.find_all('p',{'class':'_2xg6Ul'})[0].text
            except:
                comment_heading='No comment Heading'

            try:
                comtag=comment_box.div.div.find_all('div', {'class': ''})
                comment=comtag[0].div.text
            except:
                comment='No comments'

            try:
                rating=comment_box.div.div.div.find_all('div',{'class':"hGSR34 E_uFuv"})[0].text
            except:
                rating='Not Rated'

            try:
                customer_name=comment_box.div.div.find_all('p',{'class':'_3LYOAd _3sxSiS'})[0].text
            except:
                customer_name='unknown'

            reviews={'product':search_string,
                     'customer_name':customer_name,
                     'Rating':rating,
                     'comment_heading':comment_heading,
                     'comments':comment
                     }
            all_reviews.append(reviews)
    return all_reviews





#obtain_product_reviews(search_string)

#obtain_product_reviews(search_string)
