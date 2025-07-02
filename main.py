import flet as ft

def main(page : ft.Page):
    
    
    
    page.bgcolor="#ffffff"
    page.padding=0
    
    
    def resizing(e):
        page_image.width=page.width
        page_image.height=page.height
        
        page_image.update()
        
    page.on_resized=resizing
    
    
    page.fonts={
        "Russon": "fonts/RussoOne-Regular.ttf"
    }
    
    page.theme = ft.Theme(font_family="Russon")
    
    
    name=ft.Image("favicon.png", width=50, height=50)
    
    about_me=ft.Text("Hi, I'm Anshul", size=50)
    
    page_image=ft.Image("images/portfolio_design2.png", fit=ft.ImageFit.COVER, width=page.width, height=page.height)
    
    all_stack=ft.Stack([
                page_image, 
                ft.Column([name, about_me], 
                        alignment=ft.MainAxisAlignment.CENTER,left=40, top=20, spacing=200),
                ]
            )
    page.add(all_stack)
    
    
ft.app(main, assets_dir="assets", view=ft.WEB_BROWSER, port=2005)