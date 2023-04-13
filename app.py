from flask import Flask, render_template, url_for, request,redirect
import csv

app = Flask(__name__)
print(__name__)

'''practice urls comment out if you want to use the practice html and css files'''
# @app.route('/')
# def prahome():
#     '''this function returns the html index page on the the url path which is the home page'''
#     return render_template('practice_index.html')

# @app.route('/<username>')
# def variable(username= None):
#     '''this function takes a variable in the url and renders it to our index.html page it is able to access it because of the refrencing in the html page called name'''
#     return render_template('practice_index.html', name = username)

# @app.route('/<username>/<int:post_id>')
# def sec_variable(username= None, post_id =None):
#     return render_template('practice_index.html', post = post_id, name= username)

# @app.route('/in')
# def she():
#     return render_template('practice_about.html')

# @app.route('/blog')
# def blog():
#     '''this function returns just your html page on the url path of blog'''
#     return render_template('practice_index.html')


# @app.route('/about.html')
# def about():
#     '''this function returns just your html page on the url path of about.html'''
#     return render_template('practice_about.html')

# @app.route('/blog/2020/dogs')
# def dogs():
#     '''this function returns just a text on the url path of blog/2020/dogs'''
#     return 'pictures of 2020 dogs'



'''instead of copying and pasting app routes for our various html pages 
we an dynamically use only one app route that takes a variable and render it on our url'''
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/index.html')
# def home1():
#     return render_template('index.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

'''this is the concise way of writing urls'''
@app.route('/<string:page_name>')
def change(page_name):
    return render_template(page_name)


#  getting data from user, writing it to a file and redirecting a thank you html page to the user

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = str(request.form.to_dict())
#         with open('database.txt', 'a') as file:
#             # file.write('\n')
#             file.write(f'\n{data}')
#             file.close()
                   
#         print(data)
#         # return 'thank you'
#         return redirect ('/thankyou.html')
#     else:
#         return 'something went wrong'
    
    

# another way to write the data gotten from user to a file is either csv or a file and we call the function in our approute

# def write_to_file(data):
#     with open('database.txt', 'a') as file:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
     with open('database.csv', 'a', newline='') as file:
         email = data['email']
         subject = data['subject']
         message = data['message']
         CSV = csv.writer(file, delimiter=',', quotechar='"',  quoting= csv.QUOTE_MINIMAL)
         CSV.writerow([email,subject,message])
         
         
@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data= request.form.to_dict()
        # write_to_file(data)   # uncomment its function above for it work
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'     
         
         
         
if __name__ == "__main__":
    app.run(debug=True)