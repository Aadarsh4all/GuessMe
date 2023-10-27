import flet as ft
from random import randint

class myClassName:
 
    def main(page: ft.Page):
        page.title = "GUESS ME"
        DoublePlayer_LL = 0
        DoublePlayer_UL = 0
        
        
    #######################################################################################################################
    # UNIVERSAL ELEMENTS
    #######################################################################################################################
        # Fonts
        page.fonts = {
            "fnt_Reydex" : "fonts/Reydex-vm6xM.otf",
            "fnt_Ubuntu" : "fonts/ubuntu.ttf",
            "fnt_MonoT"  : "fonts/MonoT.ttf"
        }
      
        
        # SinglePlayer Alert Menu ##################################################
        def SinglePlayer_AlertMenu_dismissed(e):
            print("SinglePlayer Alert Menu Dismissed!")

        def show_SinglePlayer_AlertMenu(e):
            SinglePlayer_AlertMenu.open = True
            SinglePlayer_AlertMenu.update()

        def close_SinglePlayer_AlertMenu(e):
            SinglePlayer_AlertMenu.open = False
            SinglePlayer_AlertMenu.update()
        
        SinglePlayer_AlertMenu = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [
                        ft.Text("This is sheet's content!"),
                        ft.ElevatedButton("Close bottom sheet", on_click=close_SinglePlayer_AlertMenu),
                    ],
                    tight=True,
                ),
                padding=20,
                width=300,
                height=180
            ),
            open=True,
            on_dismiss=SinglePlayer_AlertMenu_dismissed,
        )
        
        page.overlay.append(SinglePlayer_AlertMenu)
        ##################################################################
        
        
        
        
        
        # DoublePlayer Alert Menu ##################################################
        DoublePlayer_Game_LowerLimit_input = ft.TextField(label="Lower Limit", width=300)
        DoublePlayer_Game_UpperLimit_input = ft.TextField(label="Upper Limit", width=300)

        print("Lower Limits",DoublePlayer_Game_LowerLimit_input.value)
        print("Upper Limits",DoublePlayer_Game_UpperLimit_input.value)
        
        #DoublePlayer_lowerLimit = int(DoublePlayer_Game_LowerLimit_input.value)
        #DoublePlayer_upperLimit = int(DoublePlayer_Game_UpperLimit_input.value)
       
            
        def DoublePlayer_StartGame(e):
            # DoublePlayer_lowerLimit = DoublePlayer_Game_LowerLimit_input.value
            # DoublePlayer_upperLimit = DoublePlayer_Game_UpperLimit_input.value
                
            DoublePlayer_LL = int(DoublePlayer_Game_LowerLimit_input.value)
            DoublePlayer_UL = int(DoublePlayer_Game_UpperLimit_input.value)
            
            print(f"pp ll", DoublePlayer_LL)
            print(f"pp ul", DoublePlayer_UL)
            
            page.go("/DoublePlayer")
            page.banner.open = False
            
            
            page.update()

        page.banner = ft.Banner(
            bgcolor= "#272727",
            #leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
            content=ft.Text("Set LIMITS,",font_family="fnt_MonoT", size=20),
            actions=[
              
                ft.Row([ft.Container(width=20),DoublePlayer_Game_LowerLimit_input,ft.Container(width=5)]),
                ft.Container(height=5),
                ft.Row([ft.Container(width=20),DoublePlayer_Game_UpperLimit_input,ft.Container(width=5)]),
                ft.Container(height=10),
                ft.Row([ft.Container(width=20),ft.ElevatedButton("START", on_click=DoublePlayer_StartGame, width=300),ft.Container(width=10)]),
                ft.Container(height=20)
            ],
        )

        def show_banner_click(e):
            page.banner.open = True
            page.update()
        
        
        
        # def DoublePlayer_AlertMenu_dismissed(e):
        #     print("DoublePlayer Alert Menu Dismissed!")

        # def show_DoublePlayer_AlertMenu(e):
        #     DoublePlayer_AlertMenu.open = True
        #     DoublePlayer_AlertMenu.update()

        # # def Start_DoublePlayer_AlertMenu(e):
        # #     DoublePlayer_AlertMenu.open = False
        # #     DoublePlayer_AlertMenu.update()

        # def goToDoublePlayer(e):
        #   page.go("/DoublePlayer")
        
        # DoublePlayer_AlertMenu = ft.BottomSheet(
        #     ft.Container(
        #         ft.Column(
        #             [
        #                 ft.Text("This is sheet's content!"),
        #                 DoublePlayer_Game_LowerLimit_input,
        #                 DoublePlayer_Game_UpperLimit_input,
        #                 ft.ElevatedButton("Start", on_click=goToDoublePlayer),
        #             ],
        #             tight=False,
        #         ),
        #         width=300,
        #         height=250,
        #         padding=20,
        #     ),
        #     open=True,
        #     dismissible=True,
        #     on_dismiss=DoublePlayer_AlertMenu_dismissed,
        # )
        
        # page.overlay.append(DoublePlayer_AlertMenu)
        ##################################################################
        
        
        
    #########################################################################################################################
    #########################################################################################################################

      #Answers
        DoublePlayer_AnswerRand = randint(DoublePlayer_LL,DoublePlayer_UL)
        SinglePlayer_AnswerRand = randint(1,100)







    #########################################################################################################################
    # Menu Elemts
    #########################################################################################################################
        
        # buttons
        btn1 = ft.ElevatedButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(f"Single Player", font_family="fnt_MonoT", size=25, text_align="CENTER"),
                            # ft.ListTile(
                            #     title=ft.Text("The Enchanted "),
                            #     subtitle=ft.Text(
                            #         "Music by Julie "
                            #     ),
                            # ),
                        ], alignment="center",
                    ),
                    width=120,
                    height=130,
                    padding=-8,
                    #on_click=show_SinglePlayer_AlertMenu
                    on_click=lambda _: page.go("/SinglePlayer")
                ),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                #style=ft.ButtonStyle(shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)})
            )
        
        btn2 = ft.ElevatedButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(f" 1 vs 1", font_family="fnt_MonoT", size=25, text_align="CENTER"),
                            # ft.ListTile(
                            #     title=ft.Text("The Enchanted "),
                            #     subtitle=ft.Text(
                            #         "Music by Julie "
                            #     ),
                            # ),
                        ], alignment="center",
                    ),
                    width=120,
                    height=130,
                    padding=2,
                    on_click=show_banner_click,
                    #on_click=lambda _: page.go("/DoublePlayer")
                    
                ),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                #style=ft.ButtonStyle(shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)})
            )
        
        
        btn3 = ft.ElevatedButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(f"       Costom Game", font_family="fnt_MonoT", size=20, text_align="CENTER"), ft.Text(f"                Coming Soon", font_family="fnt_MonoT", size=12)
                            # ft.ListTile(
                            #     title=ft.Text("The Enchanted "),
                            #     subtitle=ft.Text(
                            #         "Music by Julie "
                            #     ),
                            # ),
                        ], alignment="center",
                    ),
                    width=300,
                    height=70,
                    #padding=20
                    on_click=lambda _: page.go("/")
                ), 
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                #style=ft.ButtonStyle(shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)})
            )
        
        
        
        btn4 = ft.ElevatedButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(f"    Online Multiplayer", font_family="fnt_MonoT", size=20, text_align="CENTER"), ft.Text(f"                Coming Soon", font_family="fnt_MonoT", size=12)
                            # ft.ListTile(
                            #     title=ft.Text("The Enchanted "),
                            #     subtitle=ft.Text(
                            #         "Music by Julie "
                            #     ),
                            # ),
                        ], alignment="center",
                    ),
                    width=300,
                    height=70,
                    #padding=20
                    on_click=lambda _: page.go("/")
                ), 
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                #style=ft.ButtonStyle(shape={ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)})
            )
        
        # AppBar #############################
        MENU_AppBar = ft.AppBar(
            leading=ft.IconButton(ft.icons.NUMBERS_SHARP),
            leading_width=70,
            title=ft.Text("~ Guess Me", weight=ft.FontWeight.W_100, font_family="fnt_MonoT", size=16),
            center_title=True,
            bgcolor="#363636",
            toolbar_height=40,
            actions=[
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#fd5754" , icon_size=18 , tooltip="End"    , width=25),
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#febb40" , icon_size=18 , tooltip="Pause"  , width=25),
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#34c848" , icon_size=18 , tooltip="Resume" , width=25), 
                ft.Text("", width=18)

                # ft.PopupMenuButton(
                #     items=[
                #         ft.PopupMenuItem(text="Item 1"),
                #         ft.PopupMenuItem(),  # divider
                #         ft.PopupMenuItem(
                #             text="Checked item", checked=False
                #         ),
                #     ]
                # ),
            ], 
        )
        #######################################
        
        
    #########################################################################################################################
    ######################################################################################################################### 
        
        
    #########################################################################################################################
    #SINGLE PLAYER ELEMENTS (1vsComp)
    ######################################################################################################################### 
        
        
        # Player Text Feild
        SinglePlayer_check_player1 = ft.TextField(hint_text="Guess A Number", label="Player 1", width=230)
        
        # Result
        SinglePlayer_result = ft.Text(font_family="fnt_Ubuntu", size=18)
        
        print(f"=>", "SINGLE PLAYER :", SinglePlayer_AnswerRand)
        
        # Check Answer Player1
        def checkAns_player1(e):
          if float(SinglePlayer_check_player1.value ) > SinglePlayer_AnswerRand:
              SinglePlayer_result.value = "Guess A Lower Value"
              
          elif float(SinglePlayer_check_player1.value ) < SinglePlayer_AnswerRand:
              SinglePlayer_result.value = "Guess A Higher Value"
              
          elif float(SinglePlayer_check_player1.value ) == SinglePlayer_AnswerRand:
              SinglePlayer_result.value = "Yep! Player 1 Won The Match"
              
          else:
              SinglePlayer_result.value = "Oh! Something Went Wrong."
          
          page.update()
        
        # Player Enter Btn
        SinglePlayer_btn_player1 = ft.OutlinedButton("Guess", on_click=checkAns_player1)
        
        # Page Heading
        SinglePlayer_heading = ft.Card(
                      ft.Container(
                          content=
                          ft.Row(
                          controls= [ft.Text(f"GUESS ME ", font_family="fnt_Reydex", size=30,)],
                          alignment = "center",
                          ), padding=10
                      )
                  )
        
        
        
        # AppBar #############################
        SinglePlayer_AppBar = ft.AppBar(
            leading=ft.IconButton(ft.icons.NUMBERS_SHARP),
            leading_width=70,
            title=ft.Text("~ Guess Me", weight=ft.FontWeight.W_100, font_family="fnt_MonoT", size=16),
            center_title=True,
            bgcolor="#363636",
            toolbar_height=40,
            actions=[
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#fd5754" , icon_size=18 , tooltip="End"    , width=25),
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#febb40" , icon_size=18 , tooltip="Pause"  , width=25),
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#34c848" , icon_size=18 , tooltip="Resume" , width=25), 
                ft.Text("", width=18)

                # ft.PopupMenuButton(
                #     items=[
                #         ft.PopupMenuItem(text="Item 1"),
                #         ft.PopupMenuItem(),  # divider
                #         ft.PopupMenuItem(
                #             text="Checked item", checked=False
                #         ),
                #     ]
                # ),
            ], 
        )
        ##########################################
        
    #########################################################################################################################
    ######################################################################################################################### 




    #########################################################################################################################
    #DOUBLE PLAYER ELEMENTS (1vs1)
    ######################################################################################################################### 
        
        
        # Player Text Feild
        DoublePlayer_check_player1 = ft.TextField(hint_text="Guess A Number", label="Player 1", width=230)
        DoublePlayer_check_player2 = ft.TextField(hint_text="Guess A Number", label="Player 2", width=230)

        # Result
        DoublePlayer_result = ft.Text(font_family="fnt_Ubuntu", size=18)
        
        print(f"=>", "DOUBLE PLAYER :", DoublePlayer_AnswerRand)
        
        # Check Answer Player1
        def DoublePlayer_checkAns_player1(e):
          if float(DoublePlayer_check_player1.value ) > DoublePlayer_AnswerRand:
              DoublePlayer_result.value = "Guess A Lower Value"
              
          elif float(DoublePlayer_check_player1.value ) < DoublePlayer_AnswerRand:
              DoublePlayer_result.value = "Guess A Higher Value"
              
          elif float(DoublePlayer_check_player1.value ) == DoublePlayer_AnswerRand:
              DoublePlayer_result.value = "Yep! Player 1 Won The Match"
              
          else:
              DoublePlayer_result.value = "Oh! Something Went Wrong."
          
          page.update()
          
        # Check Answer Player2
        def DoublePlayer_checkAns_player2(e):
          if float(DoublePlayer_check_player2.value ) > DoublePlayer_AnswerRand:
              DoublePlayer_result.value = "Guess A Lower Value"
              
          elif float(DoublePlayer_check_player2.value ) < DoublePlayer_AnswerRand:
              DoublePlayer_result.value = "Guess A Higher Value"
              
          elif float(DoublePlayer_check_player2.value ) == DoublePlayer_AnswerRand:
              DoublePlayer_result.value = "Yep! Player 2 Won The Match"
              
          else:
              DoublePlayer_result.value = "Oh! Something Went Wrong."
          
          page.update()
        
        # Player Enter Btn
        DoublePlayer_btn_player1 = ft.OutlinedButton("Guess", on_click=DoublePlayer_checkAns_player1)
        DoublePlayer_btn_player2 = ft.OutlinedButton("Guess", on_click=DoublePlayer_checkAns_player2)
        
        # Page Heading
        DoublePlayer_heading = ft.Card(
                      ft.Container(
                          content=
                          ft.Row(
                          controls= [ft.Text(f"GUESS ME ", font_family="fnt_Reydex", size=30,)],
                          alignment = "center",
                          ), padding=10
                      )
                  )
        
        # AppBar #############################
        DoublePlayer_AppBar = ft.AppBar(
            leading=ft.IconButton(ft.icons.NUMBERS_SHARP),
            leading_width=70,
            title=ft.Text("~ Guess Me", weight=ft.FontWeight.W_100, font_family="fnt_MonoT", size=16),
            center_title=True,
            bgcolor="#363636",
            toolbar_height=40,
            actions=[
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#fd5754" , icon_size=18 , tooltip="End"    , width=25),
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#febb40" , icon_size=18 , tooltip="Pause"  , width=25),
                ft.IconButton(ft.icons.CIRCLE_ROUNDED , icon_color="#34c848" , icon_size=18 , tooltip="Resume" , width=25), 
                ft.Text("", width=18)

                # ft.PopupMenuButton(
                #     items=[
                #         ft.PopupMenuItem(text="Item 1"),
                #         ft.PopupMenuItem(),  # divider
                #         ft.PopupMenuItem(
                #             text="Checked item", checked=False
                #         ),
                #     ]
                # ),
            ], 
        )
        ##########################################
    #########################################################################################################################
    ######################################################################################################################### 




    #########################################################################################################################
    #COUSTOM GAME ELEMENTS (Player's Choice)
    ######################################################################################################################### 
    #########################################################################################################################
    ######################################################################################################################### 
        
        
        
        
        
        
        
        
        
    #########################################################################################################################
    # ROUTING ELEMENTS for Page Navigation
    ######################################################################################################################### 
        def route_change(route):
            page.views.clear()
            
            ################################################
            # Setting-UP Menu Page
            ################################################
            page.views.append(
                ft.View(
                    "/",
                    [
                        MENU_AppBar,
                        ft.Container(height=20),#spaces
                        
                        ft.Column([ft.Row([btn1,btn2],alignment="center")]),
                        ft.Container(height=20),#spaces
                        
                        ft.Column([ft.Row([btn3],alignment="center")]),
                        ft.Container(height=20),#spaces
                        
                        ft.Column([ft.Row([btn4],alignment="center")]),
                        ft.Container(height=20),#spaces
                        
                        #ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                    ],
                )
            )
            ################################################
            ################################################
            
          
            
            
            ################################################
            # Setting-UP Single Player Page
            ################################################
            if page.route == "/SinglePlayer":
                page.views.append(
                    ft.View(
                        "/SinglePlayer",
                        [
                            SinglePlayer_AppBar,
                            ft.Container(height=25),#spaces
                        
                            ft.Column([ft.Row([SinglePlayer_check_player1,SinglePlayer_btn_player1],alignment="center")]),
                            ft.Container(content=SinglePlayer_result, padding=30),
                        ], horizontal_alignment="CENTER"
                    )
                )
            ################################################
            ################################################
            
            
            
            ################################################
            # Setting-UP Double Player (1vs1) Page
            ################################################
            elif page.route == "/DoublePlayer":
                page.views.append(
                    ft.View(
                        "/DoublePlayer",
                        [
                            DoublePlayer_AppBar,
                            ft.Container(height=25),#spaces
                        
                            ft.Column([ft.Row([DoublePlayer_check_player1,DoublePlayer_btn_player1],alignment="center")]),
                            ft.Column([ft.Row([DoublePlayer_check_player2,DoublePlayer_btn_player2],alignment="center")]),
                            
                            ft.Container(content=DoublePlayer_result, padding=30),
                        ], horizontal_alignment="CENTER"
                    )
                )
            ################################################
            ################################################
            
            
            ################################################
            # Setting-UP Custom Game (Player's Choice) Page
            ################################################
            ################################################
            ################################################
            
            
            page.update()

        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)
    #########################################################################################################################
    ######################################################################################################################### 

    ft.app(target=main, view=ft.AppView.WEB_BROWSER)