import os
import sqlite3 as sql
from os import urandom
from soduko_version3 import grid_creater
from flask import Flask, session,  request, redirect, url_for
from db import *




app = Flask(__name__)

app.debug = True
app.secret_key = urandom(24)


@app.route('/')
def index():
    if 'email' in session:
        redirect(url_for('game'))
        
    return """ 
<!DOCTYPE html>
<html lang="en">
<head>
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="./static/javaskript.js"></script>
  <link rel="stylesheet" href="./static/soduko.css">
  <title>WELCOME PAGE</title>
</head>
<body id="mainpage" >
 <h1>Welcome to C<>DEdoku</h1>
 <p>register or sign in to play the C<>DEdoku game</p>
 <button id="main_screen_button" onclick='location.replace("/register")'>Register</button>
 <button id="main_screen_button" onclick='location.replace("/sign_in")'>Sign in</button> 
</body>
</html>

    
    
"""
         

@app.route('/register')
def register():
    if 'email' in session:
        return redirect(url_for('game'))
        # return 'Hey, {}!'.format(escape(session['username']))
    else:


         return """   
         <!DOCTYPE html>
<html lang="en">
<head>
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="./static/javaskript.js"></script>
  <link rel="stylesheet" href="./static/soduko.css">
  <title>WELCOME PAGE</title>
</head>
<body id="mainpage" >
     <form action="/new_user" method="post" id="register">
               <p>Username </p><input name="name" id = "register_form" type="text" required>
               <p>Email </p><input name="email" id = "register_form" type="email" required>
               <p>Password </p><input name="password" id = "register_form" type="password" required>
               <button id="main_screen_button2" >Register</button>
               
               
     </form>
</body>
</html>  
     
          """



@app.route('/sign_in_check', methods=['GET', 'POST'])
def sign_in_check():
    if request.method == 'POST':
         if 'email' in session:
              return redirect(url_for('game'))
              
         else:
               
               email = request.form['email']
               password = request.form['password']
               
               login_data=get_db('SELECT email, password FROM users WHERE email = "{}" and password = "{}"'.format(email,password))
               if len(login_data )!=0 :
                    session['email'] = request.form['email']
                    return redirect(url_for('game'))
                    
               else:
                    
                    return redirect(url_for('register'))
                   


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():           
                           
    return '''
        <form action="/sign_in_check" method="post">
            <p>Username <input name="email"></p>
            <p>Password <input name="password"></p>
            <button type="submit">Sign in</button>
            
            
        </form>
    '''


@app.route('/sign_out')
def sign_out():
    session.pop('email',None )
    return redirect(url_for('index'))


@app.route('/new_user',methods = ['POST', 'GET'])
def addrec():
     
     if request.method == 'POST':
          name = request.form['name']
          email = request.form['email']
          password = request.form['password']
          insert_db('INSERT INTO users (name , email, password) VALUES("{}","{}","{}")'.format(name,email,password))
          session['email'] = request.form['email']
     return redirect(url_for('game'))  



@app.route('/Congratulations')
def congradulations():
     if "email" not in session:
          return redirect(url_for('index'))
     else:
          return """
         <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="./static/javaskript.js"></script>
  <link rel="stylesheet" href="./static/soduko.css">
  <title>Document</title>
</head>
<body id="congratulations" >
<div id="mainMassege">
 <h1>Congratulations</h1> 
 <p>you solved the C<>DEoku Puzzle</p>
</div>
</body>
</html>
"""



    
@app.route('/game')
def game():
     if "email" not in session:
          
          return redirect(url_for('index'))
     else:
          json_variable = grid_creater()
      
          return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="./static/javaskript.js"></script>
  <link rel="stylesheet" href="./static/soduko.css">
  <title>Document</title>
</head>
<body onload="" >

  <form action="" id="gamegrid">
    <table class="tb2">
    <h1>
      <caption>C<>DEdoku</caption>
      <tbody>
        <tr>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="0" maxlength="1" type="text" oninput="checkCell(this.id,this.value)"  
                       value={json_variable["1,1"]}></td>
                  <td><input class="general"id="1" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,2"]}></td>
                  <td><input class="general"id="2" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="9" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,4"]}></td>
                  <td><input class="general"id="10" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,5"]}></td>
                  <td><input class="general"id="11" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="18" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,7"]}></td>
                  <td><input class="general"id="19" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,8"]}></td>
                  <td><input class="general"id="20" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["1,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="3" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,1"]}></td>
                  <td><input class="general"id="4" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,2"]}></td>
                  <td><input class="general"id="5" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="12" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,4"]}></td>
                  <td><input class="general"id="13" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,5"]}></td>
                  <td><input class="general"id="14" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="21" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,7"]}></td>
                  <td><input class="general"id="22" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,8"]}></td>
                  <td><input class="general"id="23" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["2,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="6" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,1"]}></td>
                  <td><input class="general"id="7" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,2"]}></td>
                  <td><input class="general"id="8" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="15" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,4"]}></td>
                  <td><input class="general"id="16" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,5"]}></td>
                  <td><input class="general"id="17" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="24" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,7"]}></td>
                  <td><input class="general"id="25" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,8"]}></td>
                  <td><input class="general"id="26" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["3,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="27" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,1"]}></td>
                  <td><input class="general"id="28" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,2"]}></td>
                  <td><input class="general"id="29" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="36" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,4"]}></td>
                  <td><input class="general"id="37" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,5"]}></td>
                  <td><input class="general"id="38" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="45" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,7"]}></td>
                  <td><input class="general"id="46" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,8"]}></td>
                  <td><input class="general"id="47" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["4,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="30" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,1"]}></td>
                  <td><input class="general"id="31" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,2"]}></td>
                  <td><input class="general"id="32" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="39" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,4"]}></td>
                  <td><input class="general"id="40" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,5"]}></td>
                  <td><input class="general"id="41" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="48" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,7"]}></td>
                  <td><input class="general"id="49" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,8"]}></td>
                  <td><input class="general"id="50" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["5,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="33" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,1"]}></td>
                  <td><input class="general"id="34" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,2"]}></td>
                  <td><input class="general"id="35" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="42" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,4"]}></td>
                  <td><input class="general"id="43" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,5"]}></td>
                  <td><input class="general"id="44" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="51" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,7"]}></td>
                  <td><input class="general"id="52" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,8"]}></td>
                  <td><input class="general"id="53" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["6,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="54" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,1"]}></td>
                  <td><input class="general"id="55" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,2"]}></td>
                  <td><input class="general"id="56" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="63" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,4"]}></td>
                  <td><input class="general"id="64" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,5"]}></td>
                  <td><input class="general"id="65" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="72" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,7"]}></td>
                  <td><input class="general"id="73" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,8"]}></td>
                  <td><input class="general"id="74" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["7,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="57" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,1"]}></td>
                  <td><input class="general"id="58" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,2"]}></td>
                  <td><input class="general"id="59" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="66" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,4"]}></td>
                  <td><input class="general"id="67" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,5"]}></td>
                  <td><input class="general"id="68" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="75" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,7"]}></td>
                  <td><input class="general"id="76" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,8"]}></td>
                  <td><input class="general"id="77" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["8,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
          <td>
            <table>
              <tbody>
                <tr>
                  <td><input class="general"id="60" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,1"]}></td>
                  <td><input class="general"id="61" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,2"]}></td>
                  <td><input class="general"id="62" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,3"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="69" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,4"]}></td>
                  <td><input class="general"id="70" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,5"]}></td>
                  <td><input class="general"id="71" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,6"]}></td>
                </tr>
                <tr>
                  <td><input class="general"id="78" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,7"]}></td>
                  <td><input class="general"id="79" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,8"]}></td>
                  <td><input class="general"id="80" maxlength="1" type="text" oninput="checkCell(this.id,this.value) "
                       value={json_variable["9,9"]}></td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </form>

  <button onclick='location.replace("/sign_out")'>sign out</button>
  <script>
    add_attribute();
    checkInputValue();
    
    </script>
</body>
</html>

                """


              
               
               


if __name__ == "__main__":
    app.run()

    

    
