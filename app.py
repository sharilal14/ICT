from flask import Flask,request,render_template,redirect
import pickle
import numpy as np
# FLASK WEB APP
app=Flask(__name__)
model=pickle.load(open('PHISHING_model.pkl','rb'))
@app.route('/')
def home():
  return render_template("home.html",)
# WEB APP
@app.route('/check',methods=['POST'])
def check():
  #text
  url_name=request.values['url_name']
  domain_name=request.values['domain_name']
  #number
  len_large_line=request.values['len_large_line']
  line_of_code=request.values['line_of_code']
  #boolean
  has_images=request.values['has_images']
  has_css=request.values['has_css']
  has_js=request.values['has_js']
  has_self_references=request.values['has_self_references']
  has_external_references=request.values['has_external_references']
  is_social_net=request.values['is_social_net']
  has_copyright_info=request.values['has_copyright_info']
  has_description=request.values['has_description']
  has_submit_button=request.values['has_submit_button']

  
# HAS IMAGES
  if has_images=="YES":
    has_images=1
  else:
    has_images=0    
# HAS CSS
  if has_css=="YES":
    has_css=1
  else:
    has_css=0    
# HAS JS
  if has_js=="YES":
    has_js=1
  else:
    has_js=0  
# HAS SELF REFERENCES
  if has_self_references=="YES":
    has_self_references=1
  else:
    has_self_references=0  
# HAS EXTERNAL REFERENCES
  if has_external_references=="YES":
    has_external_references=1
  else:
    has_external_references=0  
# IS SOCIAL NETOWRK
  if is_social_net=="YES":
    is_social_net=1
  else:
    is_social_net=0  
# HAS COPY_RIGHT_INFO
  if has_copyright_info=="YES":
    has_copyright_info=1
  else:
    has_copyright_info=0
# HAS DESCRIPTION  
  if has_description=="YES":
    has_description=1
  else:
    has_description=0
# HAS SUBMIT BUTTON
  if has_submit_button=="YES":
    has_submit_button=1
  else:
    has_submit_button=0  
# IS HTTPS:
  part1 = url_name.split("//")[0]
  if part1=="https:":
    is_https=1
  else:
    is_https=0
# URL SIMILARITY INDEX
  part2 = url_name.split("//")[1]
  if part2==domain_name:
    URL_SIMILARITY_INDEX = 1
  else:
    URL_SIMILARITY_INDEX = 0
# ENTER DETAILS
  print(f"url_name                ->{url_name}")
  print(f"domain_name             ->{domain_name}")
  print(f"len_large_line          ->{len_large_line}")
  print(f"line_of_code            ->{line_of_code}")
  print(f"has_images              ->{has_images}")
  print(f"has_css                 ->{has_css}")
  print(f"has_js                  ->{has_js}")
  print(f"has_self_references     ->{has_self_references}")
  print(f"has_external_references ->{has_external_references}")
  print(f"is_social_net           ->{is_social_net}")
  print(f"has_description         ->{has_description}")
  print(f"has_copyright_info      ->{has_copyright_info}")
  print(f"has_submit_button       ->{has_submit_button}")
# ENTERED VALUED
  values_taken=[URL_SIMILARITY_INDEX,
                line_of_code, 
                has_self_references, 
                has_images,
                has_css,
                has_js,
                has_external_references,
                is_social_net,
                has_copyright_info,
                len_large_line,
                has_description,
                has_submit_button]
  
  """  
  //CODE FOR PREDICTING WITH MODEL   
  """
  features = np.array([[URL_SIMILARITY_INDEX,line_of_code,has_images,has_css,is_social_net,has_self_references,has_js,has_description,has_copyright_info,is_https,has_external_references,len_large_line,has_submit_button ]])
  prediction = model.predict(features)
  result = prediction
# RESULT
  if result==0:
    result_display=f"IT MIGHT BE A PHISHING URL"
  else:
    result_display=f"IT MIGHT NOT BE A PHISHING URL"

  return render_template("result.html",values_taken=values_taken,result_display=result_display)
# WEB APP EXECUTION
if __name__=='__main__':
  app.run(debug=True)
