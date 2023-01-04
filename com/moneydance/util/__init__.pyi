from typing import Callable, Iterator, List, TypeVar
import com.infinitekind.moneydance.model
import com.infinitekind.util
import com.moneydance.apps.md.view.resources

T = TypeVar("T")


class BasePropertyChangeReporter:
    pass
    
class CompoundIterator(Iterator):
    def __init__(self, iterator: Iterator['T'], iterator2: Iterator['T']): ...
    
    def hasNext(self) -> bool: ...
    
    def next(self) -> 'T': ...
    
    def remove(self) -> None: ...
    
    
class Constants:
    BACKSLASH = '\\'
    MILLIS_PER_DAY = '86400000'
    
    def __init__(self): ...
    
    
class CustomDateFormat:
    def __init__(self, s: str): ...
    
    def format(self, i: int) -> str: ...
    
    def getPattern(self) -> str: ...
    
    @staticmethod
    def guessCenturyForYear(i: int) -> int: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    def parse(self, s: str) -> 'java.util.Date': ...
    
    def parseInt(self, s: str) -> int: ...
    
    def setShowDay(self, b: bool) -> None: ...
    
    def setShowYear(self, b: bool) -> None: ...
    
    
class DateUtils:
    def __init__(self): ...
    
    @staticmethod
    def daysBetween(j: 'java.util.Date', j2: 'java.util.Date') -> int: ...
    
    @staticmethod
    def daysInPeriodType(j: 'java.util.Date', c: com.infinitekind.moneydance.model.PeriodType) -> int: ...
    
    @staticmethod
    def decrement(j: 'java.util.Date', i: int, i2: int) -> 'java.util.Date': ...
    
    @staticmethod
    def decrementDateByPeriod(j: 'java.util.Date', c: com.infinitekind.moneydance.model.PeriodType) -> 'java.util.Date': ...
    
    @staticmethod
    def decrementMonth(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def decrementWeek(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def decrementYear(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def getBeginningOfWeek(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def getCurrentMonth() -> int: ...
    
    @staticmethod
    def getCurrentWeek() -> int: ...
    
    @staticmethod
    def getCurrentYear() -> int: ...
    
    @staticmethod
    def getFirstDayInPeriod(j: 'java.util.Date', c: com.infinitekind.moneydance.model.PeriodType) -> 'java.util.Date': ...
    
    @staticmethod
    def getFirstDayOfFirstWeekInMonth(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def getFirstDayOfYear(i: int) -> 'java.util.Date': ...
    
    @staticmethod
    def increment(j: 'java.util.Date', i: int, i2: int) -> 'java.util.Date': ...
    
    @staticmethod
    def incrementDateByPeriod(j: 'java.util.Date', c: com.infinitekind.moneydance.model.PeriodType) -> 'java.util.Date': ...
    
    @staticmethod
    def incrementDay(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def incrementMonth(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def incrementWeek(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def incrementYear(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def monthByIndexFromDate(i: int, j: 'java.util.Date') -> 'java.util.Date': ...
    
    
class DeepClone:
    def __init__(self): ...
    
    def deepClone(self) -> object: ...
    
    
class IOUtils:
    def __init__(self): ...
    
    @staticmethod
    def copy(j: 'java.io.File', j2: 'java.io.File') -> None: ...
    
    @staticmethod
    def copyDirectoryContents(j: 'java.io.File', j2: 'java.io.File') -> None: ...
    
    @staticmethod
    def copyFile(j: 'java.io.File', j2: 'java.io.File') -> None: ...
    
    @staticmethod
    def copyFolder(j: 'java.io.File', j2: 'java.io.File') -> None: ...
    
    @staticmethod
    def copyStream(j: 'java.io.InputStream', j2: 'java.io.OutputStream') -> int: ...
    
    @staticmethod
    def createTempFolder() -> 'java.io.File': ...
    
    @staticmethod
    def delete(j: 'java.io.File') -> None: ...
    
    @staticmethod
    def deleteFile(j: 'java.io.File') -> None: ...
    
    @staticmethod
    def deleteFolder(j: 'java.io.File') -> None: ...
    
    @staticmethod
    def isDirectoryEmpty(j: 'java.io.File') -> bool: ...
    
    @staticmethod
    def renameFilesMatching(s: str, s2: str, j: 'java.io.File') -> None: ...
    
    @staticmethod
    def zipRecursively(j: 'java.util.zip.ZipOutputStream', j2: 'java.io.File', j3: 'java.io.FilenameFilter') -> None: ...
    
    
class Misc:
    def __init__(self): ...
    
    @staticmethod
    def addNoDuplicates(list: List['T'], t: 'T') -> bool: ...
    
    @staticmethod
    def isEqual(t: 'T', t2: 'T') -> bool: ...
    
    @staticmethod
    def isZero(list: List[int], i: int) -> bool: ...
    
    
class Platform:
    def __init__(self): ...
    
    @staticmethod
    def architecture() -> str: ...
    
    @staticmethod
    def isArm() -> bool: ...
    
    @staticmethod
    def isBigSurOrLater() -> bool: ...
    
    @staticmethod
    def isIntel() -> bool: ...
    
    @staticmethod
    def isMac() -> bool: ...
    
    @staticmethod
    def isOSX() -> bool: ...
    
    @staticmethod
    def isOSXVersionAtLeast(s: str) -> bool: ...
    
    @staticmethod
    def isUnix() -> bool: ...
    
    @staticmethod
    def isWindows() -> bool: ...
    
    
    class Architecture:
        arm32 = 'arm32'
        arm64 = 'arm64'
        intel32 = 'intel32'
        intel64 = 'intel64'
        unknown = 'unknown'
        
        def __init__(self): ...
        
        @staticmethod
        def fromPropertyString(s: str) -> str: ...
        
        @staticmethod
        def valueOf(s: str) -> str: ...
        
        @staticmethod
        def values() -> List[str]: ...
        
        
    
class Sorting:
    def __init__(self): ...
    
    @staticmethod
    def sort(list: List[int]) -> None: ...
    
    
class StreamObject(com.infinitekind.util.StreamObject):
    def __init__(self): ...
    
    
class StreamTable(com.infinitekind.util.StreamTable):
    def __init__(self): ...
    
    def fromkeys(self): ...
    
    
class StreamUtil(com.infinitekind.util.StreamUtil):
    def __init__(self): ...
    
    
class StreamVector(com.infinitekind.util.StreamVector):
    def __init__(self): ...
    
    
class StringEncodingException(com.infinitekind.util.StringEncodingException):
    def __init__(self): ...
    
    
class StringUtils(com.infinitekind.util.StringUtils):
    def __init__(self): ...
    
    
class UiUtil:
    DLG_HGAP = 10
    DLG_VGAP = 8
    HGAP = 8
    LABEL_COLON = u'labelColon'
    TEXT_ANTIALIAS_HINT = 'Antialiased text mode'
    VGAP = 4
    
    def __init__(self): ...
    
    @staticmethod
    def addLabelSuffix(c: com.moneydance.apps.md.view.resources.MDResourceProvider, s: str) -> str: ...
    
    @staticmethod
    def getLabelText(c: com.moneydance.apps.md.view.resources.MDResourceProvider, s: str) -> str: ...
    
    @staticmethod
    def moveOnScreen(j: 'java.awt.Point', j2: 'java.awt.Rectangle') -> 'java.awt.Point': ...
    
    @staticmethod
    def runOnUIThread(callable: Callable) -> None: ...
    
    
class VersionVerifierCallback:
    def __init__(self): ...
    
    def errorCheckingVersion(self, s: str) -> None: ...
    
    def userHasCurrentVersion(self) -> None: ...
    
    def userHasOldVersion(self, s: str, s2: str, list: List[str]) -> None: ...
    
    
