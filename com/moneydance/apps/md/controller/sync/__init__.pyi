from typing import Callable, List
import com.infinitekind.moneydance.model
import com.infinitekind.tiksync
import com.moneydance.apps.md.controller
import com.moneydance.apps.md.view.gui
import com.moneydance.apps.md.view.gui.sync


class AbstractSyncFolder(com.infinitekind.tiksync.SyncFolder):
    def __init__(self): ...
    
    def cloneSyncFolder(self) -> 'AbstractSyncFolder': ...
    
    def delete(self, s: str) -> None: ...
    
    def encryptBytes(self, list: List[int]) -> List[int]: ...
    
    def getFileTimestamp(self, s: str) -> int: ...
    
    def getSubpath(self) -> str: ...
    
    def getSyncTypeID(self) -> str: ...
    
    def listSubfolders(self, s: str) -> List[str]: ...
    
    def listTxnFiles(self) -> List[str]: ...
    
    def readFile(self, s: str) -> 'java.io.InputStream': ...
    
    def readUnencrypted(self, s: str) -> 'java.io.InputStream': ...
    
    def setSubpath(self, s: str) -> None: ...
    
    def writeFile(self, s: str, j: 'java.io.File') -> None: ...
    
    def writeUnencryptedFile(self, s: str, j: 'java.io.InputStream') -> None: ...
    
    
class DocumentFolderSyncer(com.infinitekind.moneydance.model.TransactionListener, com.infinitekind.moneydance.model.AccountListener):
    BASE_STATE_FILENAME = u'mdata-v1'
    ENCRYPTION_TEST_STRING = u'Hello, how are you?'
    LABEL_FILENAME = u'mdsyncinfo.txt'
    
    def __init__(self, c: com.moneydance.apps.md.controller.AccountBookWrapper): ...
    
    def accountAdded(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def accountBalanceChanged(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def accountDeleted(self, c: com.infinitekind.moneydance.model.Account, c2: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def accountModified(self, c: com.infinitekind.moneydance.model.Account) -> None: ...
    
    def performSyncing(self, c: com.infinitekind.tiksync.SyncStorage, abstractSyncFolder: AbstractSyncFolder, abstractSyncFolder2: AbstractSyncFolder) -> None: ...
    
    def transactionAdded(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    def transactionModified(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    def transactionRemoved(self, c: com.infinitekind.moneydance.model.AbstractTxn) -> None: ...
    
    
class DropboxAPISyncFolder(AbstractSyncFolder):
    SYNC_TYPE = u'dropbox_api'
    
    def __init__(self, c: 'com.dropbox.core.v2.DbxClientV2', s: str): ...
    
    def createParents(self) -> None: ...
    
    def delete(self, s: str) -> None: ...
    
    def exists(self, s: str) -> bool: ...
    
    def getFileTimestamp(self, s: str) -> int: ...
    
    def getModified(self, s: str) -> 'java.util.Date': ...
    
    def getPathToDocFile(self, s: str) -> str: ...
    
    def getSyncTypeID(self) -> str: ...
    
    def listFiles(self, s: str) -> List[str]: ...
    
    def listSubfolders(self, s: str) -> List[str]: ...
    
    def listTxnFiles(self) -> List[str]: ...
    
    def readFile(self, s: str) -> 'java.io.InputStream': ...
    
    def toString(self) -> str: ...
    
    def writeFile(self, s: str, j: 'java.io.File') -> None: ...
    
    
class EncryptedSyncFolder(AbstractSyncFolder):
    def __init__(self, abstractSyncFolder: AbstractSyncFolder, mDSyncCipher: 'MDSyncCipher'): ...
    
    def createParents(self) -> None: ...
    
    def delete(self, s: str) -> None: ...
    
    def encryptBytes(self, list: List[int]) -> List[int]: ...
    
    def exists(self, s: str) -> bool: ...
    
    def getFileTimestamp(self, s: str) -> int: ...
    
    def getModified(self, s: str) -> 'java.util.Date': ...
    
    def getSubpath(self) -> str: ...
    
    def getSyncTypeID(self) -> str: ...
    
    def listFiles(self, s: str) -> List[str]: ...
    
    def listSubfolders(self, s: str) -> List[str]: ...
    
    def listTxnFiles(self) -> List[str]: ...
    
    def readFile(self, s: str) -> 'java.io.InputStream': ...
    
    def readUnencrypted(self, s: str) -> 'java.io.InputStream': ...
    
    def setSubpath(self, s: str) -> None: ...
    
    def toString(self) -> str: ...
    
    def writeFile(self, s: str, j: 'java.io.File') -> None: ...
    
    def writeUnencryptedFile(self, s: str, j: 'java.io.InputStream') -> None: ...
    
    
class GenericFSSyncFolder(AbstractSyncFolder):
    def __init__(self, s: str, j: 'java.io.File'): ...
    
    def canDisconnect(self) -> bool: ...
    
    def createParents(self) -> None: ...
    
    def delete(self, s: str) -> None: ...
    
    def disconnect(self) -> None: ...
    
    def exists(self, s: str) -> bool: ...
    
    def getFileTimestamp(self, s: str) -> int: ...
    
    def getModified(self, s: str) -> 'java.util.Date': ...
    
    def getSyncBaseFolder(self) -> 'java.io.File': ...
    
    def getSyncTypeID(self) -> str: ...
    
    def isConnected(self) -> bool: ...
    
    def listFiles(self, s: str) -> List[str]: ...
    
    def listSubfolders(self, s: str) -> List[str]: ...
    
    def listTxnFiles(self) -> List[str]: ...
    
    def readFile(self, s: str) -> 'java.io.InputStream': ...
    
    def syncingStopped(self) -> None: ...
    
    def toString(self) -> str: ...
    
    def writeFile(self, s: str, j: 'java.io.File') -> None: ...
    
    
class ICloudContainer:
    def __init__(self): ...
    
    def blockUntilAvailabilityIsKnown(self) -> bool: ...
    
    def createParents(self, s: str) -> None: ...
    
    def delete(self, s: str) -> None: ...
    
    def exists(self, s: str) -> bool: ...
    
    def getAvailability(self) -> str: ...
    
    @staticmethod
    def getInstance() -> 'ICloudContainer': ...
    
    def getModified(self, s: str) -> 'java.util.Date': ...
    
    def isContainerAvailable(self) -> bool: ...
    
    def listFiles(self, s: str) -> List[str]: ...
    
    def listSubfolders(self, s: str) -> List[str]: ...
    
    def readFile(self, s: str) -> 'java.io.InputStream': ...
    
    def toString(self) -> str: ...
    
    def writeFile(self, s: str, j: 'java.io.InputStream') -> bool: ...
    
    
    class ICloudAvailability:
        AVAILABLE = 'AVAILABLE'
        NOT_AVAILABLE = 'NOT_AVAILABLE'
        UNKNOWN = 'UNKNOWN'
        
        def __init__(self): ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class ICloudSyncFolder(AbstractSyncFolder):
    SYNC_TYPE = u'icloud'
    
    def __init__(self, iCloudContainer: ICloudContainer, s: str): ...
    
    def createParents(self) -> None: ...
    
    def delete(self, s: str) -> None: ...
    
    def exists(self, s: str) -> bool: ...
    
    def getFileTimestamp(self, s: str) -> int: ...
    
    def getModified(self, s: str) -> 'java.util.Date': ...
    
    def getSyncTypeID(self) -> str: ...
    
    def listFiles(self, s: str) -> List[str]: ...
    
    def listSubfolders(self, s: str) -> List[str]: ...
    
    def listTxnFiles(self) -> List[str]: ...
    
    def readFile(self, s: str) -> 'java.io.InputStream': ...
    
    def toString(self) -> str: ...
    
    def writeFile(self, s: str, j: 'java.io.File') -> None: ...
    
    
class MDSyncCipher:
    def __init__(self): ...
    
    def cloneCipher(self) -> 'MDSyncCipher': ...
    
    @staticmethod
    def decryptBytes(list: List[int], s: str) -> List[int]: ...
    
    @staticmethod
    def encryptString(s: str, s2: str) -> List[int]: ...
    
    @staticmethod
    def getSyncCipher(s: str) -> 'MDSyncCipher': ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    
class NetRequest:
    HDR_CONTENT_LENGTH = u'Content-Length'
    HDR_CONTENT_TYPE = u'Content-Type'
    
    def __init__(self): ...
    
    def beginOKResponse(self) -> bool: ...
    
    def beginResponse(self, i: int, s: str) -> bool: ...
    
    def flush(self) -> None: ...
    
    def getRequestContentLength(self) -> int: ...
    
    def initialize(self, j: 'java.net.Socket') -> bool: ...
    
    def matchesRequest(self, s: str, s2: str) -> bool: ...
    
    def out(self) -> 'java.io.BufferedWriter': ...
    
    def putHeader(self, s: str, s2: str) -> None: ...
    
    def rawIn(self) -> 'java.io.InputStream': ...
    
    def rawOut(self) -> 'java.io.OutputStream': ...
    
    @staticmethod
    def readAll(j: 'java.io.InputStream', j2: 'java.lang.StringBuffer') -> str: ...
    
    @staticmethod
    def readAllBytes(j: 'java.io.InputStream', i: int) -> List[int]: ...
    
    @staticmethod
    def readLine(j: 'java.io.InputStream', j2: 'java.lang.StringBuffer') -> str: ...
    
    def sendNotFoundResponse(self) -> bool: ...
    
    def setOutputStream(self, j: 'java.io.OutputStream') -> None: ...
    
    def toString(self) -> str: ...
    
    
class SyncManager(com.moneydance.apps.md.controller.AppEventListener):
    DEBUG = False
    
    def __init__(self, c: com.moneydance.apps.md.view.gui.MoneydanceGUI): ...
    
    def dataFileWasLoaded(self, c: com.moneydance.apps.md.controller.AccountBookWrapper) -> None: ...
    
    def getData(self) -> com.moneydance.apps.md.controller.AccountBookWrapper: ...
    
    def getSyncMethod(self) -> com.moneydance.apps.md.view.gui.sync.SyncFolderConfigurer: ...
    
    def handleEvent(self, s: str) -> None: ...
    
    def loadSyncFolderForData(self, c: com.moneydance.apps.md.controller.AccountBookWrapper) -> com.moneydance.apps.md.view.gui.sync.SyncFolderConfigurer: ...
    
    def showSyncSettings(self, c: com.moneydance.apps.md.view.gui.MoneydanceGUI, j: 'java.awt.Frame') -> None: ...
    
    def syncSettingsWereChanged(self) -> bool: ...
    
    
class SyncSettingsWindow(com.moneydance.apps.md.view.gui.SecondaryDialog):
    pass
    
class SyncStateWriter:
    def __init__(self, c: com.moneydance.apps.md.controller.AccountBookWrapper): ...
    
    def writeTo(self, j: 'java.io.Writer') -> None: ...
    
    
class SyncTxn:
    attributes = '<reflected field public java.util.HashMap com.moneydance.apps.md.controller.sync.SyncTxn.attributes at 0xafe>'
    txnType = '<reflected field public java.lang.String com.moneydance.apps.md.controller.sync.SyncTxn.txnType at 0xaff>'
    
    def __init__(self): ...
    
    def copyInto(self, syncTxn: 'SyncTxn') -> None: ...
    
    @staticmethod
    def decodeHexByte(i: int, i2: int) -> int: ...
    
    def getInt(self, o: object, i: int) -> int: ...
    
    def getLong(self, o: object, i: int) -> int: ...
    
    def getStr(self, o: object, s: str) -> str: ...
    
    def getSubset(self, s: str) -> 'SyncTxn': ...
    
    def readAttributes(self, j: 'java.io.InputStream') -> bool: ...
    
    def readAttributesFromString(self, s: str) -> bool: ...
    
    def toString(self) -> str: ...
    
    @staticmethod
    def unescapeURLTxt(s: str) -> str: ...
    
    def writeAttributes(self, j: 'java.io.OutputStream') -> None: ...
    
    @staticmethod
    def writeEscapedTxt(j: 'java.io.OutputStream', o: object) -> None: ...
    
    
class SyncTxnReaderX(Callable):
    def __init__(self): ...
    
    def getTimestampForObjectWithGUID(self, s: str) -> int: ...
    
    def run(self) -> None: ...
    
    
