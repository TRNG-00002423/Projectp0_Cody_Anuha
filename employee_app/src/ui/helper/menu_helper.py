from pyfiglet import FigletFont, Figlet

class MenuHelper():
    WIDTH = 60
    WIDTH_2 = (int)(WIDTH * (2/3))
    FIGLET = Figlet(font="smslant")
    
    @staticmethod
    def display_header_1(text : str):
        text = text.strip()
        fig_text = MenuHelper.FIGLET.renderText(text).rstrip() + "\n"
        print("=" * MenuHelper.WIDTH)
        print("=" * MenuHelper.WIDTH)
        print(fig_text)
        print("=" * MenuHelper.WIDTH)
        print("=" * MenuHelper.WIDTH)

    @staticmethod
    def display_header_2(text : str) :
        text = text.strip()
        print("-" * MenuHelper.WIDTH_2)
        print(text.center(MenuHelper.WIDTH_2, " "))
        print("-" * MenuHelper.WIDTH_2)
    
    @staticmethod
    def display_header_2_with_menu(menu_name : str, text : str):
        text = text.strip()
        menu_name = menu_name.strip()
        menu_name = "[" + menu_name + "]"
        print("-" * MenuHelper.WIDTH_2)
        print(menu_name.center(MenuHelper.WIDTH_2), " ")
        print(text.center(MenuHelper.WIDTH_2, " "))
        print("-" * MenuHelper.WIDTH_2)
    
    @staticmethod
    def display_numbered_list(ls : list):
        for i, v in enumerate(ls, start=1):
            print(f"{i}. {v}")
    
    @staticmethod
    def display_paired_numbered_list(paired_ls : list):
        for i, v in enumerate(paired_ls, start=1):
            print(f"{i}. {v[0]}\n{v[1]}")

if __name__ == "__main__":
    MenuHelper.display_header_1("Welcome!")
    MenuHelper.display_header_2("Main Menu")
    
    ls = ["Edit Files", "View Submitted Files", "Exit Menu"]
    MenuHelper.display_numbered_list(ls)