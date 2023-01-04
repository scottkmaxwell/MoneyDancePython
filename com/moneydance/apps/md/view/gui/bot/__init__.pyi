from typing import Callable, List
import com.infinitekind.moneydance.model
import com.moneydance.apps.md.controller.bot
import com.moneydance.apps.md.controller.olb
import com.moneydance.apps.md.view.gui


class BrowserContext:
    def __init__(self): ...
    
    def closeBrowser(self) -> None: ...
    
    def getBook(self) -> com.infinitekind.moneydance.model.AccountBook: ...
    
    def getGUI(self) -> com.moneydance.apps.md.view.gui.MoneydanceGUI: ...
    
    def handleDownloadedFile(self, c: com.moneydance.apps.md.controller.olb.HttpCollector) -> bool: ...
    
    def setStatus(self, s: str, f: float) -> None: ...
    
    
class MoneyBotWindow(com.moneydance.apps.md.view.gui.SecondaryFrame, Callable):
    pass
    
class PythonInterface(com.moneydance.apps.md.controller.bot.MoneybotInterface):
    def __init__(self, c: com.moneydance.apps.md.view.gui.MoneydanceGUI, c2: com.infinitekind.moneydance.model.AccountBook): ...
    
    def accountsWithType(self, s: str) -> List[com.infinitekind.moneydance.model.Account]: ...
    
    def closeWebBot(self) -> None: ...
    
    def getAccountForID(self, s: str) -> com.infinitekind.moneydance.model.Account: ...
    
    def getField(self, o: object, s: str, s2: str, s3: str, s4: str, b: bool) -> str: ...
    
    def getWebBot(self) -> com.moneydance.apps.md.controller.bot.RobotWebSession: ...
    
    def setField(self, o: object, s: str, s2: str, b: bool) -> None: ...
    
    
class WebBrowserListener:
    def __init__(self): ...
    
    def errorOccurred(self, s: str, j: 'java.lang.Throwable') -> None: ...
    
    def locationChanged(self, s: str) -> None: ...
    
    def logEvent(self, s: str) -> None: ...
    
    def progressUpdated(self, j: 'java.lang.Number') -> None: ...
    
    def statusChanged(self, s: str) -> None: ...
    
    def titleChanged(self, s: str) -> None: ...
    
    
class WebView(com.moneydance.apps.md.view.gui.SecondaryFrame, 'javax.swing.event.HyperlinkListener'):
    pass
    
