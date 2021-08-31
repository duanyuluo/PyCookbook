#encoding=utf-8

def probe_var(var):
    return "-> %s %s" % (var, type(var))

class IntroductionChapter(object):
    intro_width = 80

    def __init__(self, chapter) -> None:
        super().__init__()
        self.chapter = chapter
        self.section_idx = 0

    def intro(self, *args):
        print(*args)

    def intro_chapter(self, *args):
        print("*" * IntroductionChapter.intro_width)
        print("*" + str.center(self.chapter, IntroductionChapter.intro_width-2) + "*")
        for arg in args:
            for ln in str.splitlines(arg):
                print("* " + str.ljust(ln, IntroductionChapter.intro_width-3) + "*")
        print("*" * IntroductionChapter.intro_width)

    def section(self, *args):
        self.section_idx += 1
        str_section = "[#%s]" % self.section_idx
        print("-" * (IntroductionChapter.intro_width - len(str_section)) + str_section)
        self.intro(*args)

    def code(self, *args):
        pass

def new_intro(chapter_name):
    return IntroductionChapter(chapter_name)
