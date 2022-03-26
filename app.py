from pywebio.input import *
from pywebio.output import *
from pywebio import start_server, session
from summarizer import *

def main():  # PyWebIO application function
    session.set_env(title='Summarizer', output_animation=False)
    put_html("<h1> Our Awesome Text Summarizer Tool </h1>")
    
    text= textarea(label="Paste your text here", rows=8, minlength=20)
    summary= generate_summary_from_text(text)
    wordcloud_img = open('./wordcloud.png', 'rb').read()
    put_image(wordcloud_img, width='100%', height='100%')
    put_html(f"<h1> Summary: </h1><p>{summary}</p>")
       
    
    
start_server(main, port=8000)