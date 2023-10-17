import os
import re

def wrap():
    if os.name != 'nt':
        home_dir = os.path.expanduser("~")
        profile = os.path.join(home_dir, '.profile')
        if not os.path.exists(profile):
            with open(profile, 'w') as f:
                f.write("# Empty profile file.")
        
        with open(profile, 'r') as f:
            text = f.read()
            regex = r"# pvw wrapper start\n(.+?)\n# pvw wrapper end"
            with open('magic.sh') as m:
                content = m.read()
                if re.search(regex, text, re.DOTALL):
                    new_text = re.sub(regex, content, text, flags=re.DOTALL)
                else:
                    new_text = text + f"\n\n{content}"
        
        with open(profile, 'w') as f:
            f.write(new_text)

        os.system(f". {profile}")



if __name__ == '__main__':
    wrap()