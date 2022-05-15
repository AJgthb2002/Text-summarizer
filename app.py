from pywebio.input import *
from pywebio.output import *
from pywebio import start_server, session
from summarizer import *
import pyperclip as pc

header_img = open('images/nutshell_header.png', 'rb').read()
welcome_img= open('images/Nutshell.jpg', 'rb').read()

def menu():
    
    input_choice = input_group('Get Started', [
    actions('', [ 
        {'label': 'Upload a file', 'value': 1}, 
        {'label': 'Enter text', 'value': 2}, 
        ], name='action', help_text=None),
    ])

    user_inp= input_choice["action"]
    if user_inp==1:
        clear("main")
        with use_scope("ROOT",clear=True):
            put_image(header_img, width='100%', height='100%', position=0)
        f = file_upload("Upload a text file", accept=".txt", max_size='10M',required=True) 
        l= input("Length of summary (No. of sentences) ", type=NUMBER)                 
        userfile= open('datafiles/'+f['filename'], 'wb').write(f['content'])  
        summary= generate_summary_from_file('datafiles/'+f['filename'], top_n=l)
        wordcloud_img = open('./wordcloud.jpg', 'rb').read()
        clear("main")
        with use_scope("main",clear=True):
            put_image(wordcloud_img, width='100%', height='100%')
            put_html(f"<h1> Summary: </h1><p>{summary}</p>")
        
        selected_opt=None
        while(selected_opt!=3):
            summary_choice = input_group('', [
            actions('', [ 
                {'label': 'Copy to clipboard', 'value': 1}, 
                {'label': 'Share wordcloud', 'value': 2}, 
                {'label': 'Back', 'value': 3}, 
                ], name='action', help_text=None),
            ])
            selected_opt=summary_choice["action"]
            if selected_opt==1:
                pc.copy(summary)
                with use_scope("main"):
                    put_success("Copied to Clipboard!")
            elif selected_opt==2:
                pass 
            elif selected_opt==3:
                clear("main")
                clear("ROOT")
        return 

    if user_inp==2:
        clear("main")
        with use_scope("ROOT",clear=True):
            put_image(header_img, width='100%', height='100%', position=0)
        text= textarea(label="Paste your text here", rows=8, minlength=20)
        l= input("Length of summary (No. of sentences) ", type=NUMBER)        
        summary= generate_summary_from_text(text, top_n=l)
        wordcloud_img = open('./wordcloud.jpg', 'rb').read()
        clear("main")
        with use_scope("main",clear=True):
            put_image(wordcloud_img, width='100%', height='100%')
            put_html(f"<h1> Summary: </h1><p>{summary}</p>")
        
        selected_opt=None
        while(selected_opt!=3):
            summary_choice = input_group('', [
            actions('', [ 
                {'label': 'Copy to clipboard', 'value': 1}, 
                {'label': 'Share wordcloud', 'value': 2}, 
                {'label': 'Back', 'value': 3}, 
                ], name='action', help_text=None),
            ])
            selected_opt=summary_choice["action"]
            if selected_opt==1:
                pc.copy(summary)
                with use_scope("main"):
                    put_success("Copied to Clipboard!")
            elif selected_opt==2:
                pass 
            elif selected_opt==3:
                clear("main")
                clear("ROOT")
        return        


def main():  # PyWebIO application function
    session.set_env(title='Nutshell', output_animation=False)
    # put_html("<h1> Nutshell Text Summarizer Tool </h1>")
    
    while(True):
        with use_scope("main",clear=True):
            put_image(src=welcome_img, width='120%', height='390px')  #put welcome screen
        menu()
        

    
    
    
       
    
    
start_server(main, port=8000)