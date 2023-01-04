from typing import Dict, List, TypeVar

T = TypeVar("T")


class CustomDateFormat:
    def __init__(self, s: str): ...
    
    @staticmethod
    def dateFormatFromSystem() -> 'CustomDateFormat': ...
    
    def format(self, i: int) -> str: ...
    
    def getFieldOrderString(self) -> str: ...
    
    def getPattern(self) -> str: ...
    
    @staticmethod
    def guessCenturyForYear(i: int) -> int: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    def parse(self, s: str) -> 'java.util.Date': ...
    
    def parseInt(self, s: str) -> int: ...
    
    def setShowDay(self, b: bool) -> None: ...
    
    def setShowYear(self, b: bool) -> None: ...
    
    
class DateUtil:
    MILLIS_PER_DAY = '86400000'
    fiscalYearStartMMDD = 101
    
    def __init__(self): ...
    
    @staticmethod
    def calculateDaysBetween(i: int, i2: int) -> int: ...
    
    @staticmethod
    def calculateDaysInMonth(i: int) -> int: ...
    
    @staticmethod
    def calculateDaysInYear(i: int) -> int: ...
    
    @staticmethod
    def convertCalToInt(j: 'java.util.Calendar') -> int: ...
    
    @staticmethod
    def convertDateToInt(j: 'java.util.Date') -> int: ...
    
    @staticmethod
    def convertIntDateToLong(i: int) -> 'java.util.Date': ...
    
    @staticmethod
    def convertLongDateToInt(i: int) -> int: ...
    
    @staticmethod
    def dateIsAfterCurrentMonth(j: 'java.util.Date') -> bool: ...
    
    @staticmethod
    def decrementDate(i: int) -> int: ...
    
    @staticmethod
    def decrementMonth(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def decrementYear(i: int) -> int: ...
    
    @staticmethod
    def firstDayInFiscalQuarter(i: int) -> int: ...
    
    @staticmethod
    def firstDayInFiscalYear(i: int) -> int: ...
    
    @staticmethod
    def firstDayInMonth(i: int) -> int: ...
    
    @staticmethod
    def firstDayInQuarter(i: int) -> int: ...
    
    @staticmethod
    def firstDayInWeek(i: int) -> int: ...
    
    @staticmethod
    def firstDayInYear(i: int) -> int: ...
    
    @staticmethod
    def firstMinuteInDay(i: int) -> int: ...
    
    @staticmethod
    def getAdjustedRate(i: int, i2: int) -> float: ...
    
    @staticmethod
    def getDate(i: int, i2: int, i3: int) -> int: ...
    
    @staticmethod
    def getStrippedDate() -> int: ...
    
    @staticmethod
    def getStrippedDateInt() -> int: ...
    
    @staticmethod
    def getStrippedDateObj() -> 'java.util.Date': ...
    
    @staticmethod
    def getUniqueCurrentTimeMillis() -> int: ...
    
    @staticmethod
    def incrementDate(i: int) -> int: ...
    
    @staticmethod
    def incrementMonth(j: 'java.util.Date') -> 'java.util.Date': ...
    
    @staticmethod
    def incrementYear(i: int) -> int: ...
    
    @staticmethod
    def lastDayInFiscalQuarter(i: int) -> int: ...
    
    @staticmethod
    def lastDayInFiscalYear(i: int) -> int: ...
    
    @staticmethod
    def lastDayInMonth(i: int) -> int: ...
    
    @staticmethod
    def lastDayInQuarter(i: int) -> int: ...
    
    @staticmethod
    def lastDayInWeek(i: int) -> int: ...
    
    @staticmethod
    def lastDayInYear(i: int) -> int: ...
    
    @staticmethod
    def lastMinuteInDay(i: int) -> int: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    @staticmethod
    def minmax(i: int, i2: int, i3: int) -> int: ...
    
    @staticmethod
    def monthsInPeriod(i: int, i2: int) -> float: ...
    
    @staticmethod
    def safeRate(f: float) -> float: ...
    
    @staticmethod
    def setCalendarDate(j: 'java.util.Calendar', i: int) -> None: ...
    
    @staticmethod
    def setToBeginningOfMonth(j: 'java.util.Calendar') -> None: ...
    
    @staticmethod
    def setToEndOfMonth(j: 'java.util.Calendar') -> None: ...
    
    @staticmethod
    def stripTimeFromCal(j: 'java.util.Calendar') -> None: ...
    
    @staticmethod
    def stripTimeFromDate(i: int) -> int: ...
    
    @staticmethod
    def yearsInPeriod(i: int, i2: int) -> float: ...
    
    
    class Comparator:
        def __init__(self): ...
        
        
    
class IOUtils:
    ATOMIC_RENAME_METHOD_NAME = u'renameAtomicallyWithNIO'
    
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
    def deleteFolder(j: 'java.io.File') -> bool: ...
    
    @staticmethod
    def getUnusedFileNameWithBaseAndExtension(j: 'java.io.File', s: str, s2: str) -> 'java.io.File': ...
    
    @staticmethod
    def isDirectoryEmpty(j: 'java.io.File') -> bool: ...
    
    @staticmethod
    def openZip(j: 'java.io.File', s: str) -> str: ...
    
    @staticmethod
    def readFileFully(s: str) -> List[int]: ...
    
    @staticmethod
    def readFully(j: 'java.io.File') -> List[int]: ...
    
    @staticmethod
    def readline(j: 'java.io.InputStream') -> str: ...
    
    @staticmethod
    def readlines(j: 'java.io.InputStream') -> List[str]: ...
    
    @staticmethod
    def renameFilesMatching(s: str, s2: str, j: 'java.io.File') -> None: ...
    
    @staticmethod
    def renameMostlyAtomicallyWithoutNIO(j: 'java.io.File', j2: 'java.io.File') -> None: ...
    
    @staticmethod
    def unzip(j: 'java.io.InputStream', j2: 'java.io.File') -> bool: ...
    
    @staticmethod
    def writeAtomically(s: str, j: 'java.io.File') -> None: ...
    
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
    
    
class StreamObject:
    def __init__(self): ...
    
    def isStreamTable(self) -> bool: ...
    
    def isStreamVector(self) -> bool: ...
    
    def readFrom(self, s: str) -> None: ...
    
    def readTheRest(self, j: 'java.io.Reader') -> None: ...
    
    def writeTo(self, j: 'java.io.Writer') -> None: ...
    
    def writeToString(self) -> str: ...
    
    
class StreamTable(StreamObject, dict):
    def __init__(self): ...
    
    def deepClone(self) -> 'StreamTable': ...
    
    def fromkeys(self): ...
    
    def getBoolean(self, o: object, b: bool) -> bool: ...
    
    def getInt(self, o: object, i: int) -> int: ...
    
    def getKeyArray(self) -> List[str]: ...
    
    def getLong(self, o: object, i: int) -> int: ...
    
    def getStr(self, o: object, s: str) -> str: ...
    
    def getStrList(self, o: object) -> List[str]: ...
    
    def isStreamTable(self) -> bool: ...
    
    def isStreamVector(self) -> bool: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    def merge(self, d: dict) -> None: ...
    
    def put(self, o: object, i: int) -> None: ...
    
    def readFrom(self, s: str) -> None: ...
    
    def readFromFile(self, s: str) -> None: ...
    
    def readTheRest(self, j: 'java.io.Reader') -> None: ...
    
    def setField(self, o: object, list: List[str]) -> None: ...
    
    def startingDelimiter(self) -> int: ...
    
    def toString(self) -> str: ...
    
    def writeTo(self, j: 'java.io.OutputStream') -> None: ...
    
    def writeToFile(self, s: str) -> None: ...
    
    def writeToString(self) -> str: ...
    
    
class StreamUtil:
    def __init__(self): ...
    
    @staticmethod
    def encodeString(s: str) -> str: ...
    
    @staticmethod
    def getNonWhitespace(j: 'java.io.Reader') -> int: ...
    
    @staticmethod
    def readString(j: 'java.io.Reader') -> str: ...
    
    @staticmethod
    def readUndelimitedString(j: 'java.io.Reader', i: int) -> str: ...
    
    @staticmethod
    def writeString(s: str, j: 'java.io.Writer') -> None: ...
    
    
class StreamVector(StreamObject, list):
    def __init__(self): ...
    
    def deepClone(self) -> 'StreamVector': ...
    
    def isStreamTable(self) -> bool: ...
    
    def isStreamVector(self) -> bool: ...
    
    def readFrom(self, s: str) -> None: ...
    
    def readTheRest(self, j: 'java.io.Reader') -> None: ...
    
    def startingDelimiter(self) -> int: ...
    
    def writeTo(self, j: 'java.io.Writer') -> None: ...
    
    def writeToString(self) -> str: ...
    
    
class StringEncodingException(Exception):
    def __init__(self): ...
    
    
class StringUtils:
    def __init__(self): ...
    
    @staticmethod
    def areStringsIdentical(s: str, s2: str) -> bool: ...
    
    @staticmethod
    def base64Encode(s: str) -> str: ...
    
    @staticmethod
    def capitalizeFirst(s: str) -> str: ...
    
    @staticmethod
    def combineWords(list: List[str]) -> str: ...
    
    @staticmethod
    def computeLevenshteinDistance(j: 'java.lang.CharSequence', j2: 'java.lang.CharSequence') -> int: ...
    
    @staticmethod
    def convertToFileName(s: str) -> str: ...
    
    @staticmethod
    def countFields(s: str, i: int) -> int: ...
    
    @staticmethod
    def decode(s: str) -> str: ...
    
    @staticmethod
    def decodeHex(s: str) -> List[int]: ...
    
    @staticmethod
    def decodeURL(s: str) -> str: ...
    
    @staticmethod
    def doNothing() -> None: ...
    
    @staticmethod
    def encode(s: str) -> str: ...
    
    @staticmethod
    def encodeHex(list: List[int], b: bool) -> str: ...
    
    @staticmethod
    def fieldIndex(s: str, i: int, i2: int) -> str: ...
    
    @staticmethod
    def fillLeft(s: str, i: int, i2: int) -> str: ...
    
    @staticmethod
    def fillRight(s: str, i: int, i2: int) -> str: ...
    
    @staticmethod
    def formatFixedDecimals(s: str, i: int, i2: int) -> str: ...
    
    @staticmethod
    def formatMinDecimals(s: str, i: int, i2: int) -> str: ...
    
    @staticmethod
    def formatPercentage(f: float, i: int) -> str: ...
    
    @staticmethod
    def formatRate(f: float, i: int) -> str: ...
    
    @staticmethod
    def formatShortRate(f: float, i: int) -> str: ...
    
    @staticmethod
    def getAppropriateRateFormat(f: float, i: int) -> 'java.text.DecimalFormat': ...
    
    @staticmethod
    def getExtensionFromFilename(s: str) -> str: ...
    
    @staticmethod
    def getGMTDateStr(j: 'java.util.Date') -> str: ...
    
    @staticmethod
    def getNLengthString(i: int, i2: int) -> str: ...
    
    @staticmethod
    def getNonNull(s: str) -> str: ...
    
    @staticmethod
    def guessDecimalType(s: str) -> int: ...
    
    @staticmethod
    def isAllNumber(s: str) -> bool: ...
    
    @staticmethod
    def isBlank(s: str) -> bool: ...
    
    @staticmethod
    def isDate(s: str) -> bool: ...
    
    @staticmethod
    def isEmpty(s: str) -> bool: ...
    
    @staticmethod
    def isInteger(s: str) -> bool: ...
    
    @staticmethod
    def isNumeric(s: str) -> bool: ...
    
    @staticmethod
    def join(list: List[str], s: str) -> str: ...
    
    @staticmethod
    def looksLikeEmailAddress(s: str) -> bool: ...
    
    @staticmethod
    def looksLikeFormula(s: str) -> bool: ...
    
    @staticmethod
    def main(list: List[str]) -> None: ...
    
    @staticmethod
    def parseDouble(s: str, i: int) -> float: ...
    
    @staticmethod
    def parseDoubleWithException(s: str, i: int) -> float: ...
    
    @staticmethod
    def parseFormula(s: str, i: int) -> float: ...
    
    @staticmethod
    def parseFraction(s: str, i: int) -> float: ...
    
    @staticmethod
    def parseQuickenDate(s: str) -> int: ...
    
    @staticmethod
    def parseRate(s: str, i: int) -> float: ...
    
    @staticmethod
    def parseURLParameters(s: str, dict: Dict[str,str]) -> None: ...
    
    @staticmethod
    def printRecentStackFrames(i: int) -> None: ...
    
    @staticmethod
    def replaceAll(s: str, s2: str, s3: str) -> str: ...
    
    @staticmethod
    def shortenStringIfLongerThan(s: str, i: int, s2: str) -> str: ...
    
    @staticmethod
    def sortStringArray(list: List[str]) -> None: ...
    
    @staticmethod
    def split(s: str, i: int) -> List[str]: ...
    
    @staticmethod
    def splitIntoList(s: str, i: int) -> List[str]: ...
    
    @staticmethod
    def stripExtension(s: str) -> str: ...
    
    @staticmethod
    def stripExtraCharacters(s: str) -> str: ...
    
    @staticmethod
    def stripNonFilenameSafeCharacters(s: str) -> str: ...
    
    @staticmethod
    def stripNonNumbers(s: str, i: int) -> str: ...
    
    @staticmethod
    def stripPath(s: str) -> str: ...
    
    @staticmethod
    def truncateHead(s: str, i: int, s2: str) -> str: ...
    
    @staticmethod
    def vectorToStringArray(l: list) -> List[str]: ...
    
    
