##Text##
import streamlit as st
 
#Title
st.title("Hello World")

#Header/Subheader
st.header("This is the header")

st.subheader("This is the subheader")

#Markdown
st.markdown("This is a markdown")

#Error/Colourful Text
st.success("Successful")

st.info("Information")

st.warning("Warning")

st.error("Error")

##Images##
from PIL import Image
img = Image.open("Assets/Images/example.jpg")
st.image(img,width=700,caption="Cute Doggo")

##Widgets##

#Checkbox
if st.checkbox("Are you awesome?"):
    st.text("yeah sure-_-")

#Radio Buttons
status = st.radio("Now, do you think you are awesome?",("Yes I am","No I am not"))

if status=="Yes I am":
    st.success("What changed in a second you dufus")
else:
    st.warning("Truth hurts my man")

#Select Box
waifu = st.selectbox("Who is your waifu",["Orihime","Kaguya","Rem","Hinata"])
st.write("Kinda cringe bro-.-")

#Slider
hot = st.slider("How hot is Aryan",1,10)

#Text Input
firstname = st.text_input("Enter your first name","Type here dufus..")

#Date Input
import datetime
the_time =  st.time_input("The time is",datetime.time())

#Displaying JSON
st.text("Display JSON")
st.json({'Name':"Aryan",'Gender':"Male"})

#Display Raw Code
st.text("Display Raw Code")
st.code("import pandas as pd")
#for a bigger code#
with st.echo(): #everthing after this will be included
    #This comment will also show
    import pandas as pd 
    df = pd.DataFrame()

#Progress Bar
import time
my_bar = st.progress(1)
for p in range(10):
    my_bar.progress(p+1)

#Spinner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished!")

#Sidebars
st.sidebar.header("About")
    