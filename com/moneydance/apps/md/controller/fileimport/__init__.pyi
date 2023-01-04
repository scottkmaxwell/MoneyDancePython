from typing import Iterable, List
import com.infinitekind.moneydance.model
import com.infinitekind.moneydance.model.txtimport
import com.infinitekind.moneydance.online
import com.moneydance.apps.md.controller
import com.moneydance.apps.md.view


class FileImportSpec:
    FILE_ENCODINGS = '[UTF-8, ISO-8859-1, US-ASCII, UTF-16, UTF-16LE, UTF-16BE]'
    
    def __init__(self, s: str, c: com.infinitekind.moneydance.online.OnlineBankingUI): ...
    
    def getColumnTypes(self) -> List[com.infinitekind.moneydance.model.txtimport.ImportFieldType]: ...
    
    def getDateFieldOrder(self) -> com.infinitekind.moneydance.model.txtimport.ImportDateFieldOrder: ...
    
    def getDecimalChar(self) -> int: ...
    
    def getDelimiter(self) -> int: ...
    
    def getDuplicateDateDiffLimit(self) -> int: ...
    
    def getFileEncoding(self) -> str: ...
    
    def getFileExtension(self) -> str: ...
    
    def getOriginalFileName(self) -> str: ...
    
    def getPossibleAccountTypes(self) -> List[str]: ...
    
    def getShouldConfirmTransactions(self) -> bool: ...
    
    def getShouldMergeTransactions(self) -> bool: ...
    
    def getSourceType(self) -> com.infinitekind.moneydance.model.txtimport.ImportDataSourceType: ...
    
    def getTargetAccount(self) -> com.infinitekind.moneydance.model.Account: ...
    
    def getUIProxy(self) -> com.infinitekind.moneydance.online.OnlineBankingUI: ...
    
    def hasSingleTargetAccount(self) -> bool: ...
    
    def setColumnTypes(self, list: List[com.infinitekind.moneydance.model.txtimport.ImportFieldType]) -> None: ...
    
    def setDateFieldOrder(self, c: com.infinitekind.moneydance.model.txtimport.ImportDateFieldOrder) -> None: ...
    
    def setDecimalChar(self, i: int) -> None: ...
    
    def setDelimiter(self, i: int) -> None: ...
    
    def setDuplicateDateDiffLimit(self, i: int) -> None: ...
    
    def setFileEncoding(self, s: str) -> None: ...
    
    def setHasSingleTargetAccount(self, b: bool) -> None: ...
    
    def setShouldConfirmTransactions(self, b: bool) -> None: ...
    
    def setShouldMergeTransactions(self, b: bool) -> None: ...
    
    def setSourceType(self, c: com.infinitekind.moneydance.model.txtimport.ImportDataSourceType) -> None: ...
    
    def setTargetAccount(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def setUIProxy(self, c: com.infinitekind.moneydance.online.OnlineBankingUI) -> None: ...
    
    def toString(self) -> str: ...
    
    
class FileImporter:
    def __init__(self): ...
    
    def doImport(self) -> None: ...
    
    def doOneStepImport(self) -> None: ...
    
    def doPrescan(self) -> bool: ...
    
    @staticmethod
    def getBestImporter(c: com.moneydance.apps.md.view.MoneydanceUI, fileImportSpec: FileImportSpec) -> 'FileImporter': ...
    
    def getBook(self) -> com.infinitekind.moneydance.model.AccountBook: ...
    
    def getInput(self) -> 'java.io.InputStream': ...
    
    def getSpec(self) -> FileImportSpec: ...
    
    def getStatusMonitor(self) -> com.moneydance.apps.md.controller.StatusMonitor: ...
    
    def init(self, c: com.infinitekind.moneydance.model.AccountBook, j: 'java.io.InputStream') -> None: ...
    
    def loadSpecFromPreferences(self, c: com.moneydance.apps.md.controller.UserPreferences) -> None: ...
    
    def saveSpecToPreferences(self, c: com.moneydance.apps.md.controller.UserPreferences) -> None: ...
    
    def setStatusMonitor(self, c: com.moneydance.apps.md.controller.StatusMonitor) -> None: ...
    
    @staticmethod
    def shouldInterceptFoundFileWithExtension(s: str) -> bool: ...
    
    
    class ImportStatus:
        FINISHED = 'FINISHED'
        IN_PROGRESS = 'IN_PROGRESS'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class OFXFileImporter(FileImporter):
    FILE_EXTENSIONS = '[ofx, qfx, ofc]'
    OFX_MIME_TYPES = '[application/vnd.intu.qbo, application/vnd.intu.ofx, application/vnd.intu.qfx, application/ofx, application/x-ofx]'
    
    def __init__(self): ...
    
    def doImport(self) -> None: ...
    
    
class QIFFileImporter(FileImporter):
    DEBUG = True
    FILE_EXTENSIONS = '[qif, qmtf]'
    QIF_IMPORT_AUTOCREATED = u'_qif_import_autocreated'
    
    def __init__(self): ...
    
    def doImport(self) -> None: ...
    
    def doPrescan(self) -> bool: ...
    
    def getImportableAccounts(self) -> Iterable[com.infinitekind.moneydance.model.Account]: ...
    
    def isAssetType(self, s: str) -> bool: ...
    
    def isLiabilityType(self, s: str) -> bool: ...
    
    
class TextFileImporter(FileImporter):
    DEFAULT_DELIMITERS = '[\t,  , ,, ., |, /, \\, -, _, *, ~, ;]'
    FILE_EXTENSIONS = '[csv, tab, tsv, txt, text]'
    MIME_TYPES = '[text/plain, text/csv]'
    
    def __init__(self): ...
    
    def doImport(self) -> None: ...
    
    def doPrescan(self) -> bool: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    
