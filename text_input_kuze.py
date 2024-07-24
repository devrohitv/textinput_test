from kivy.utils import platform
from textinput import MyTextInput

if platform == "android":
    from jnius import autoclass

class KuTextInput(MyTextInput):
    # keyboard_suggestions's on_ doesn't work..
    __events__ = ('on_suggestions', )

    def on_kv_post(self, instance):
        if platform == "android":
            self.dispatch('on_suggestions')

    def on_suggestions(self, instance=None, value=None):
        Build = autoclass("android.os.Build$VERSION")
        if Build.SDK_INT >= 33 and self.keyboard_suggestions:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Context = autoclass('android.content.Context')
            imm = PythonActivity.mActivity.getSystemService(Context.INPUT_METHOD_SERVICE)
            currentSubtype = imm.getCurrentInputMethodSubtype()

            if currentSubtype is not None:
                extra = currentSubtype.getExtraValue()
                if currentSubtype.getMode() == "keyboard" and any(["TrySuppressingImeSwitcher" in extra,
                                                                   "AsciiCapable" in extra]):
                    self.keyboard_suggestions = False
                    print("Kivys keyboard_suggestions for Gboard is now deactivated because it's already activated")
                    return
        print("No changes applied for the keyboard_suggestions.")