from selenium import webdriver
import clipboard

def communication_template(url):
    chrome = webdriver.Chrome('./Browser/Drivers/chromedriver')
    chrome.get(url)
    p = chrome.find_elements_by_tag_name("p")
    questions = ["What is Happening?","How Does This Affect Me?","Additional Information","Questions of Concerns"]
    template = """
        <h3>{q[0]}</h3> 
        <p>{p}</p> 
        <h3>{q[1]}</h3> 
        <h3>{q[2]}</h3> 
        <p>For more information on this service, please select this <a href={url}>link</a></p> 
        <h3>{q[3]}</h3> 
        <p>Please contact Ross IT Support by phone (734)-615-3000 or email RossITSupport@umich.edu</p>""".format(q = questions, p = p[2].text, url = url)

    clipboard.copy(template)
    create_html_file(template)

def create_html_file(txt):
    file = open("communication.html","w")
    file.write(txt)
    file.close()

def main():
    url = input("Please provide webpage url ==> ")
    communication_template(url)

if __name__ == "__main__":
    main()