import json
import streamlit as st
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(layout="wide")
st.markdown("""## Roadmap to Become a Web Developer""")
st.markdown("""<p style="font-weight:510">To become a full-stack web developer, you must learn a wide range of skills. Finding the right learning path and achieving a quick result can be difficult for tyros. At first, visual perception may be overwhelming in understanding what you need to learn and how everything fits together at the end.</p>""",unsafe_allow_html=True)

st.markdown("""This post includes links to great learning resources, as well as a brief description of the relevant topics, so you can get started quickly expanding your skill set.""")
st.write(" ")
with st.container():
        leftcol, centercol, rightcol = st.columns([1,3.9,1])
        with centercol:
            st.image("https://miro.medium.com/max/1400/0*ZEPJsASfB2z7hi_0")
st.write(" ")
st.markdown("""### In this blog, we will discuss the Web Development Roadmap 2022. Let’s begin!! Here’s a step-by-step process:""")
st.write(" ")

lottie_code = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tfb3estd.json")
with st.container():
    left,right = st.columns([8,9])
    with left:
        st.markdown("""
                    <ol style="font-weight:600">
                        <li>Choose a technology on which you want to work</li>
                        <li>Frontend Development</li>
                        <li>Backend Development</li>
                        <li>Database</li>
                        <li>Version Control System</li>
                    </ol>""",unsafe_allow_html=True)
    with right: 
        st_lottie(lottie_code, key="code" , height=250)
st.markdown("""#### 1. Choose a Technology""")
st.markdown("""A full-stack development comprises front-end, back-end, and database management. Choosing a technology on which you want to work depends on individuals, requirements, and applications. Few technologies on which you can work and are trending:""")
st.markdown("""
            <div style="display:flex">
            <p style="font-weight: bold">A. MERN– </p> The most popular and trending technology.
            </div>
            <ul>
                <li>
                    <div style="display:flex">
                        <p style="font-weight: bold">MongoDB– </p> A NoSQL database that deals with data.
                    </div>
                </li>
                <li>
                    <div style="display:flex">
                        <p style="font-weight: bold">Express– </p> A framework for NodeJS and handles GET, PUT, POST, DELETE functions.
                    </div>
                </li>
                <li>
                    <div style="display:flex">
                        <p style="font-weight: bold">React– </p> A JavaScript library for building User Interfaces, building single-page applications.
                    </div>
                </li>
                <li>
                    <div style="display:flex">
                        <p style="font-weight: bold">NodeJS– </p> An open-source server environment.
                    </div>
                </li>
            </ul>
            <div style="display:flex">
            <p style="font-weight: bold">B.MERN– </p> The major difference between MERN and MEAN is MERN (written in JavaScript) works on React whereas MEAN deals with Angular (a framework written in TypeScript). 
            </div>
            """,unsafe_allow_html=True)

st.write("---")
st.markdown("""#### 2. Frontend Development""")
st.markdown("""The front end is the part of a website with which the user interacts directly. The application is also known as the client side. The program provides all the users experience: text colors and styles, photos, diagrams and tables, buttons, colors and a navigation menu.""")
st.write(" ")
st.markdown("""<p style="text-align: center; font-weight:bold">Front-End Languages</p>""",unsafe_allow_html=True)
st.write(" ")
with st.container():
    left, center, right= st.columns(3)
    with left:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/FFFFFF/html-5--v1.png"/>HTML</p>""",unsafe_allow_html=True)
        st.write(" HTML stands for Hypertext Markup Language used to build the structure of a web page. HTML is used to describe the structure of information on a web page. HTML5 is the latest evolution of the standard that defines HTML.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/html/"><button class="button">HTML Doc</button></a>
        """,unsafe_allow_html=True)
    with center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/css3.png"/>CSS</p>""",unsafe_allow_html=True)
        st.write("CSS stands for Cascading Style Sheets. It is a style sheet language which is used to describe the look and formatting of a document written in markup language. CSS4 is the latest version of CSS.")

        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/css/"><button class="button">CSS Doc</button></a>
        """,unsafe_allow_html=True)

    with right:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/fluency/48/000000/javascript.png"/>JavaScript</p>""",unsafe_allow_html=True)
        st.write("This is the programming language of the web. Learn about DOM (Document Object Model), and API (Application Program Interface) properly.JavaScript is a necessary component for adding dynamic features to your website. The JavaScript programming language is based on the underlying ECMAScript specification. Learning JavaScript from the ground up is a critical step toward launching your web development career.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/js/"><button class="button">JavaScript Doc</button></a>
        """,unsafe_allow_html=True)

with st.container():
        leftcol, centercol, rightcol = st.columns([1,3.9,1])
        with centercol:
            st.image("https://miro.medium.com/max/1400/0*CsGpUYlektZNHCr4.png")
st.write(" ")
st.markdown("""<p style="text-align: center; font-weight:bold">Frontend Frameworks</p>""",unsafe_allow_html=True)
st.write(" ")
with st.container():
    left, left_center, right_center, right= st.columns(4)
    with left:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/40C057/react-native.png"/> React</p>""",unsafe_allow_html=True)
        st.write(" React is a JavaScript library for building user interfaces. React makes it painless to create interactive UIs. Design simple views for each state in your application, and React will efficiently update and render just the right components when your data changes. It is an open-source, component-based front end library responsible only for the view layer of the application. It is maintained by Facebook.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/react/"><button class="button">React Doc</button></a>
        """,unsafe_allow_html=True)

    with left_center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/angularjs.png"/>Angular</p>""",unsafe_allow_html=True)
        st.write("Angular is a platform and framework for building single-page client applications using HTML and TypeScript. Angular is written in TypeScript. It implements core and optional functionality as a set of TypeScript libraries that you import into your applications.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/angular/"><button class="button">Angular Doc</button></a>
        """,unsafe_allow_html=True)

    with right_center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> Tailwind CSS</p>""",unsafe_allow_html=True)
        st.write("Tailwind CSS is basically a utility-first CSS framework for rapidly building custom user interfaces. It is a highly customizable, low-level CSS framework that gives you all of the building blocks you need to build bespoke designs without any annoying opinionated styles you have to fight to override")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://v2.tailwindcss.com/docs"><button class="button">Tailwind CSS Doc</button></a>
        """,unsafe_allow_html=True)

    with right:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/bootstrap.png"/>Bootstrap</p>""",unsafe_allow_html=True)
        st.write("Bootstrap is a free and open-source tool collection for creating responsive websites and web applications. It is the most popular HTML, CSS, and JavaScript framework for developing responsive, mobile-first web sites.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/bootstrap/"><button class="button">Bootstrap Doc</button></a>
        """,unsafe_allow_html=True)

st.write("---")
st.markdown("""#### 3. Backend Development""")
st.markdown("""The code that runs on the server, has logic to send the appropriate data from the client and receive it from the server. Also, it includes the database which stores all of the data of the application. It consists of three parts: a server, an application, and a database. Here, the code written by developers transfers information from the database to the browser. Code written by back-end developers communicates information from the database to the browser.""")
st.write(" ")
st.markdown("""<p style="text-align: center; font-weight:bold">Backend Languages</p>""",unsafe_allow_html=True)
st.write(" ")
with st.container():
    left, left_center, right_center, right= st.columns(4)
    with left:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/ios-filled/50/000000/javascript-logo.png"/>JavaScript</p>""",unsafe_allow_html=True)
        st.write("Java script can be used as both (front end and back end) programming languages. Learning JavaScript from the ground up is a critical step toward launching your web development career. Knowledge of JavaScript is required for many frameworks on the frontend (Angular, React, Vue.js) and backend (Node.js).")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/js/"><button class="button">JS Doc</button></a>
        """,unsafe_allow_html=True)

    with left_center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/python--v1.png"/>Python</p>""",unsafe_allow_html=True)
        st.write(" Python is one of the most popular programming languages among businesses in 2020. If you haven’t yet added Python to your programming toolbox, now is the time to start. If you’re interested in learning Python for web development, you should look into Python web programming frameworks like Django or Flask.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/python/"><button class="button">Python Doc</button></a>
        """,unsafe_allow_html=True)

    with right_center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/java-coffee-cup-logo--v1.png"/>Java</p>""",unsafe_allow_html=True)
        st.write("Java is another exemplary programming language for backend web development. The object-oriented programming language is widely used for developing enterprise-scale web applications along with the development of android applications, desktop applications, scientific applications, etc.Other additional features of Java are – platform-independent, follows the OOP concepts, rich open-source libraries, automatic memory allocation & garbage collection, portability, etc.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/java/"><button class="button">Java Doc</button></a>
        """,unsafe_allow_html=True)
    with right:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/officel/16/000000/php-logo.png" width="40" height="40"/> PHP</p>""",unsafe_allow_html=True)
        st.write("PHP is an acronym for “PHP: Hypertext Preprocessor”. PHP is a server-side scripting language designed specifically for web development. Since, PHP code executed on server side so it is called server side scripting language. It is a widely-used, open source scripting language.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/php/"><button class="button">PHP Doc</button></a>
        """,unsafe_allow_html=True)
with st.container():
        leftcol, centercol, rightcol = st.columns([1,3.9,1])
        with centercol:
            st.image("https://miro.medium.com/max/1400/0*en6yuhg9GNt45wXy.png")
st.write(" ")
st.markdown("""<p style="text-align: center; font-weight:bold">Backend Frameworks</p>""",unsafe_allow_html=True)
st.write(" ")
with st.container():
    left, left_center, right_center, right= st.columns(4)
    with left:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/>Django</p>""",unsafe_allow_html=True)
        st.write(" Django is completely written in Python. If you like the elegance of the Python programming language you’ll like the Django. Django is a powerful framework and serves you for a wide range of use cases. However, if you have gained a profound understanding of Python, Django is easy to learn and you’ll discover the pragmatic approach very quickly.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/django/"><button class="button">Django Doc</button></a>
        """,unsafe_allow_html=True)
    with left_center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/nodejs.png"/> Node.js</p>""",unsafe_allow_html=True)
        st.write("Angular is a platform and framework for building single-page client applications using HTML and TypeScript. Angular is written in TypeScript. It implements core and optional functionality as a set of TypeScript libraries that you import into your applications.")
        st.markdown("""
        <style>
            .button {
            position: relative;
            background-color: rgb(255, 255, 255);
            border: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: 200;
            padding: 0.25rem 0.75rem;
            border-radius: 0.40rem;
            margin: 0px;
            width: auto;
            text-align: center;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            text-decoration: none;
            overflow: hidden;
            cursor: pointer;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
            .button:hover{
                border: 1px solid #FF4B4B;
                color : #FF4B4B;
            }
            .button:after {
            content: "";
            background: #FF4B4B;
            display: block;
            position: absolute;
            padding-top: 300%;
            padding-left: 350%;
            margin-left: -20px!important;
            margin-top: -120%;
            opacity: 0;
            transition: all 0.8s
            }
            .button:focus {
                box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                outline: none;
            }
            .button:active:after {
            padding: 0;
            margin: 0;
            opacity: 1;
            transition: 0s
            }
        </style>
        <a href="https://www.w3schools.com/nodejs/"><button class="button">Node.Js Doc</button></a>
        """,unsafe_allow_html=True)
    with right_center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/> Express</p>""",unsafe_allow_html=True)
        st.write("Express is a MEAN stack back-end component along with the AngularJS frontend framework and NoSQL databases. Express is viewed as one of the best web application development frameworks.It is used for building APIs and web applications and is considered as a standard Node.js server framework.")
        st.markdown("""
            <style>
                .button {
                position: relative;
                background-color: rgb(255, 255, 255);
                border: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: 200;
                padding: 0.25rem 0.75rem;
                border-radius: 0.40rem;
                margin: 0px;
                width: auto;
                text-align: center;
                -webkit-transition-duration: 0.4s; /* Safari */
                transition-duration: 0.4s;
                text-decoration: none;
                overflow: hidden;
                cursor: pointer;
                border: 1px solid rgba(49, 51, 63, 0.2);
                }
                .button:hover{
                    border: 1px solid #FF4B4B;
                    color : #FF4B4B;
                }
                .button:after {
                content: "";
                background: #FF4B4B;
                display: block;
                position: absolute;
                padding-top: 300%;
                padding-left: 350%;
                margin-left: -20px!important;
                margin-top: -120%;
                opacity: 0;
                transition: all 0.8s
                }
                .button:focus {
                    box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                    outline: none;
                }
                .button:active:after {
                padding: 0;
                margin: 0;
                opacity: 1;
                transition: 0s
                }
            </style>
            <a href="https://www.javatpoint.com/expressjs-tutorial"><button class="button">Express Doc</button></a>
            """,unsafe_allow_html=True)
    with right:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/laravel/laravel-plain-wordmark.svg" alt="laravel" width="40" height="40"/> Laravel</p>""",unsafe_allow_html=True)
        st.write("Node.js enables you to execute JavaScript code at the backend and is extremely powerful especially if Node.js is used together with the Express middleware. It is cross-platform runtime environment for executing JavaScript code outside a browser. You need to remember that NodeJS is not a framework and it’s not a programming language.")
        st.markdown("""
            <style>
                .button {
                position: relative;
                background-color: rgb(255, 255, 255);
                border: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: 200;
                padding: 0.25rem 0.75rem;
                border-radius: 0.40rem;
                margin: 0px;
                width: auto;
                text-align: center;
                -webkit-transition-duration: 0.4s; /* Safari */
                transition-duration: 0.4s;
                text-decoration: none;
                overflow: hidden;
                cursor: pointer;
                border: 1px solid rgba(49, 51, 63, 0.2);
                }
                .button:hover{
                    border: 1px solid #FF4B4B;
                    color : #FF4B4B;
                }
                .button:after {
                content: "";
                background: #FF4B4B;
                display: block;
                position: absolute;
                padding-top: 300%;
                padding-left: 350%;
                margin-left: -20px!important;
                margin-top: -120%;
                opacity: 0;
                transition: all 0.8s
                }
                .button:focus {
                    box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                    outline: none;
                }
                .button:active:after {
                padding: 0;
                margin: 0;
                opacity: 1;
                transition: 0s
                }
            </style>
            <a href="https://www.tutorialspoint.com/laravel/index.htm"><button class="button">Laravel Doc</button></a>
            """,unsafe_allow_html=True)
st.write("---")
st.markdown("""#### 4. Database""")
st.markdown("""The database is a collection of data from which we can manage data (store and retrieve). There are two types of databases: relational (SQL) and non-relational (NoSQL).The popular database is MySQL, MongoDB, Redis, Oracle, SQLServer and so on. As a document-type database, MongoDB, is being used more widely in Internet products.""")
st.write(" ")
with st.container():
    left, center, right= st.columns(3)
    with left:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/mysql-logo.png"/> MySQL</p>""",unsafe_allow_html=True)
        st.write("MySQL is another open-source relational database management system that is widely used for web-based applications. It is a fast and high-performance database that provides better scalability, usability, and reliability.")
        st.markdown("""
            <style>
                .button {
                position: relative;
                background-color: rgb(255, 255, 255);
                border: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: 200;
                padding: 0.25rem 0.75rem;
                border-radius: 0.40rem;
                margin: 0px;
                width: auto;
                text-align: center;
                -webkit-transition-duration: 0.4s; /* Safari */
                transition-duration: 0.4s;
                text-decoration: none;
                overflow: hidden;
                cursor: pointer;
                border: 1px solid rgba(49, 51, 63, 0.2);
                }
                .button:hover{
                    border: 1px solid #FF4B4B;
                    color : #FF4B4B;
                }
                .button:after {
                content: "";
                background: #FF4B4B;
                display: block;
                position: absolute;
                padding-top: 300%;
                padding-left: 350%;
                margin-left: -20px!important;
                margin-top: -120%;
                opacity: 0;
                transition: all 0.8s
                }
                .button:focus {
                    box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                    outline: none;
                }
                .button:active:after {
                padding: 0;
                margin: 0;
                opacity: 1;
                transition: 0s
                }
            </style>
            <a href="https://www.w3schools.com/mySQl/"><button class="button">MySQL Doc</button></a>
            """,unsafe_allow_html=True)
    with center:
        st.markdown("""<p style="text-align: center; font-weight:bold"><img src="https://img.icons8.com/color/48/000000/mongodb.png"/> MongoDB</p>""",unsafe_allow_html=True)
        st.write("MongoDB is a free and open-source document-oriented database that is very much popular among web developers. This NoSQL database uses JSON-like documents with optional schemas for storage & retrieval of data and comes up with much-needed scalability and flexibility. MongoDB provides you with numerous prominent features.")
        st.markdown("""
            <style>
                .button {
                position: relative;
                background-color: rgb(255, 255, 255);
                border: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: 200;
                padding: 0.25rem 0.75rem;
                border-radius: 0.40rem;
                margin: 0px;
                width: auto;
                text-align: center;
                -webkit-transition-duration: 0.4s; /* Safari */
                transition-duration: 0.4s;
                text-decoration: none;
                overflow: hidden;
                cursor: pointer;
                border: 1px solid rgba(49, 51, 63, 0.2);
                }
                .button:hover{
                    border: 1px solid #FF4B4B;
                    color : #FF4B4B;
                }
                .button:after {
                content: "";
                background: #FF4B4B;
                display: block;
                position: absolute;
                padding-top: 300%;
                padding-left: 350%;
                margin-left: -20px!important;
                margin-top: -120%;
                opacity: 0;
                transition: all 0.8s
                }
                .button:focus {
                    box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                    outline: none;
                }
                .button:active:after {
                padding: 0;
                margin: 0;
                opacity: 1;
                transition: 0s
                }
            </style>
            <a href="https://www.javatpoint.com/mongodb-tutorial"><button class="button">MongoDB Doc</button></a>
            """,unsafe_allow_html=True)
    with right:
        st.markdown("""<p style="text-align: center; font-weight:bold">VoltDB</p>""",unsafe_allow_html=True)
        st.write("VoltDB is a commercial in-memory DBMS that is scalable and ACID-compliant. VoltDB is designed to be a NewSQL relational database to work with mainly OLTP queries. It is designed to be a distributed database with sharding and data replication. It has both a commercial version and an open-source community version.")
        st.markdown("""
            <style>
                .button {
                position: relative;
                background-color: rgb(255, 255, 255);
                border: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: 200;
                padding: 0.25rem 0.75rem;
                border-radius: 0.40rem;
                margin: 0px;
                width: auto;
                text-align: center;
                -webkit-transition-duration: 0.4s; /* Safari */
                transition-duration: 0.4s;
                text-decoration: none;
                overflow: hidden;
                cursor: pointer;
                border: 1px solid rgba(49, 51, 63, 0.2);
                }
                .button:hover{
                    border: 1px solid #FF4B4B;
                    color : #FF4B4B;
                }
                .button:after {
                content: "";
                background: #FF4B4B;
                display: block;
                position: absolute;
                padding-top: 300%;
                padding-left: 350%;
                margin-left: -20px!important;
                margin-top: -120%;
                opacity: 0;
                transition: all 0.8s
                }
                .button:focus {
                    box-shadow: rgb(255 75 75 / 50%) 0px 0px 0px 0.2rem;
                    outline: none;
                }
                .button:active:after {
                padding: 0;
                margin: 0;
                opacity: 1;
                transition: 0s
                }
            </style>
            <a href="https://docs.voltdb.com/"><button class="button">VoltDB Doc</button></a>
            """,unsafe_allow_html=True)
st.write("---")
st.markdown("""#### 5.  Version Control""")
st.markdown("""When certain libraries are added to each application, it gets updated in a period which in turn creates a new version of it. Using Git is a very good practice if you’re working on applications. Git is an open-source platform where the entire code exists from the initial time. It is secure, flexible, easy to edit, and restores the code. It has repositories where all files including the codebase are saved and one can make changes according to the requirement. Anyone can collaborate and make changes accordingly.""")
st.write(" ")

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_vnikrcia.json")

with st.container():
    left ,right = st.columns(2)
    with left:
        st.markdown("""
                    <div style="display:flex">
                    <p style="font-weight: bold">A list of Version Control Systems are: </p>
                    </div>
                    <ol>
                        <li>
                            <div style="display:flex">
                                <p style="font-weight: bold">GitHub</p>
                            </div>
                        </li>
                        <li>
                            <div style="display:flex">
                                <p style="font-weight: bold">GitLab</p>
                            </div>
                        </li>
                        <li>
                            <div style="display:flex">
                                <p style="font-weight: bold">Beanstalk</p>
                            </div>
                        </li>
                        <li>
                            <div style="display:flex">
                                <p style="font-weight: bold">Apache Subversion</p>
                            </div>
                        </li>
                        <li>
                            <div style="display:flex">
                                <p style="font-weight: bold">Mercurial</p>
                            </div>
                        </li>
                    </ol>
                    """,unsafe_allow_html=True)
    with right:
        st_lottie(lottie_coding, key="coding" , height=300)
    
st.markdown("""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """,unsafe_allow_html=True)
st.write("---")
st.markdown("""<p style="text-align: center;"><img src="https://logodix.com/logo/70386.jpg" width="200"/></p>""",unsafe_allow_html=True)
st.markdown("""<br>""",unsafe_allow_html=True)
with st.container():
    left, center, right = st.columns(3)
    with left:
        st.markdown("""<p style="text-align: center;"><img src="https://media-exp1.licdn.com/dms/image/C4D03AQEn32MBmUBDmw/profile-displayphoto-shrink_800_800/0/1658657491591?e=1664409600&v=beta&t=8oPB_fkLyokPqBJQcCQTgOcnsqLHvfRJdxqv9RAhMj8" width="100" height="100" style="border-radius: 100px"/></p>""",unsafe_allow_html=True)
        st.markdown("""<p style="text-align: center; font-weight:bold; font-size:25px">Abhishek Malu</p>""",unsafe_allow_html=True)
        st.markdown("""I am second year Engineering student. I am a Sophomore at MBM Engineering
                        College, Jodhpur pursuing my B.Tech in Computer Science and Engineering.""")
        st.markdown("""<br>""",unsafe_allow_html=True)
    with center:
        st.markdown("""<p style="text-align: center;"><img src="https://t4.ftcdn.net/jpg/03/90/11/51/240_F_390115184_pC62LQRe5VlME5w1I1XgUxm6TeKMlQ7Q.jpg" width="200"/></p>""",unsafe_allow_html=True)
        st.markdown("""<br>""",unsafe_allow_html=True)
        st.markdown("""
                        <p style="text-align: center;color: #434A62"><img src="https://img.icons8.com/ultraviolet/40/000000/phone.png" height="30" width="30">+91-9462770492</p>
                        <p style="text-align: center;"><a href="mailto:abhimahesh49@gmail.com" style="text-decoration: none;color: #434A62"><img src="https://img.icons8.com/fluency/48/000000/mail.png" height="30" width="30"> abhishekmalu@gmail.com</a></p>
                    """,unsafe_allow_html=True)
        st.markdown("""<br>""",unsafe_allow_html=True)
    with right:
        st.markdown("""<p style="text-align: center;"><img src="https://images.assetsdelivery.com/compings_v2/aquir/aquir2009/aquir200903749.jpg" width="200"/></p>""",unsafe_allow_html=True)
        st.markdown("""<br>""",unsafe_allow_html=True)
        st.markdown("""
                    <div style="text-align: center;">
                        <a href="https://instagram.com/abhishek_maheshwari_14" target="blank"
                                style="color:red;text-decoration: none;"><img align="center"
                                    src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg"
                                    height="30" width="40" /></a>
                        <a href="https://www.linkedin.com/in/abhishek-malu-60542921a/" target="blank"><img
                                    src="https://img.icons8.com/color/48/000000/linkedin-circled--v1.png" /></a>
                        <a href="https://www.facebook.com/profile.php?id=100053538914796" target="blank"><img align="center"
                                    src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg"
                                    alt="abhishek maheshwari" height="30" width="40"></a>
                        <a href="https://twitter.com/AbhishekMalu4" target="blank"><img
                                    src="https://img.icons8.com/color/48/000000/twitter-circled--v3.png" /></a>
                    </div>
                    """,unsafe_allow_html=True)