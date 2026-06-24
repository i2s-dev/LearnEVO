# TAS Professional Error Code Table

Status: **verified** — complete 392-entry table extracted from ERRMSG.DBF (Pass 247 2026-06-24)

Source file: `\\i2s109-solidcrm\DBAMFG$\errmsg.dbf`  
Local copy: `samples/errmsg.dbf`  
Format: dBASE III+ (version 0x03), 392 records, 3 fields: ERROR_NUM (N/4), ERROR_MSG (C/64), ERROR_SZE (N/3)

The ERRMSG.DBF file stores the complete TAS Professional runtime error message table.
The ERROR_MSG field is 64 chars wide; ERROR_SZE (3 char numeric) stores the total
message length; the remaining 256 bytes of each 328-byte record hold message continuation.
Messages longer than 64 chars are reconstructed by concatenating ERROR_MSG + the
continuation bytes (no separator — the 64-char boundary falls mid-word in some entries).

---

## Categories

| Range | Category |
|-------|----------|
| 1–9 | Startup / loader errors (TASPRO.OVL, BTRIEVE) |
| 10–79 | Runtime execution errors (type mismatches, stack, arrays, files) |
| 82–158 | Btrieve I/O + general runtime messages (locks, transactions, navigation) |
| 200–232 | More Btrieve error codes with descriptive text |
| 250–279 | Navigation / lock / record state messages |
| 300–313 | Field/format size constraints (date, time, alpha, numeric sizes) |
| 500–542 | Compilation errors (source file, format, buffer, output messages) |
| 543–599 | Compiler syntax / structure error messages |
| 600–670 | Compiler field definition, library, FOR/NEXT, label errors |

---

## Complete Error Code Table

Note: Messages with a `*` suffix have minor word-break artifacts at the 64-char
field boundary (e.g., "calculat" + "s" = "calculats" instead of "calculations").
The meaning is always clear from context.

| Code | Message |
|------|---------|
| 0 | *(reserved/empty)* |
| 1 | TASPRO.OVL not found or error while loading. |
| 2 | TASHELP.OVL not found or error while loading. |
| 3 | BTRIEVE has not been loaded. |
| 4 | BTRIEVE has been removed from memory. |
| 5 | You have not specified a RUN program. |
| 6 | The RUN program specified was not found. |
| 7 | You cannot open the run program since it is locked. |
| 8 | An error occurred while reading the RUN program. |
| 9 | No memory space is available. |
| 10 | The temporary data space is too small to accomodate the calculations desired. Please specify larger in the source program. |
| 11 | You are trying to add an alphanumeric field to a numeric field. |
| 12 | The fields in this calculation are two different types. |
| 13 | The receiving and result fields in the equal command are not of same type. |
| 14 | The receiving alphanumeric field is shorter than the result being moved. |
| 15 | You are trying to save a field of a different type. |
| 16 | You have too many PUSH commands. You need to expand the size of the internal stack or change the program. |
| 17 | An Internal Stack error has occurred. Too many POPs or RETURNs. |
| 18 | There are no more temporary fields available. Please increase initial value and try again. |
| 19 | The field you are trying to use is unallocated. It may belong to a file that hasn't been opened yet, or was an array that was removed from memory — @ |
| 20 | The window title must be an ALPHA field. |
| 21 | You must have a SAVE_TO field for this command. |
| 22 | The SAVE_TO field you have specified is too small for its purpose. |
| 23 | This file number field must be of an integer type. |
| 24 | This field must be of an Integer type. |
| 25 | This field must be of a Record type. |
| 26 | The field in this command must be of an Alphanumeric type. |
| 27 | The field in this command must be a regular field; expressions or constants are not allowed. |
| 28 | The field must be of type 'F' or 'P'. |
| 29 | The receiving field in this command must be of type 'F' or 'P'. |
| 30 | The receiving field in this command must be of type 'F'. |
| 31 | The array element specified is out of range for this field. |
| 32 | File names, including paths, cannot be more than 59 chars in length — @ |
| 33 | Load file not found. |
| 34 | You already have 10 modules loaded and cannot load another. |
| 35 | Pro 5.0 Internal error #35. Please call 919-932-3068. Ask for operator 93. |
| 36 | Internal error — load bin/com routine. |
| 37 | The load number used to call the bin/com routine is not between 1 and 10 inclusive. |
| 38 | For the load number value used there is no corresponding module loaded. |
| 39 | Internal TAS-Professional 5.0 error. |
| 40 | The VALID expression returned false. The entry must be done again. |
| 41 | The field to be entered was not in the screen buffer. Please make sure you have 'MOUNTED' a screen and the field is in that screen. |
| 42 | An error has occurred while accessing a non-TAS file — @ |
| 43 | There are no more extra fields available. |
| 44 | The field you are trying to add has an unknown type. |
| 45 | The field being added cannot have a size of 0. |
| 46 | The maximum number of decimal chars for the field being added is 8. |
| 47 | An error has occurred while attempting to open FILELOC. |
| 48 | A record was not found in FILELOC for file — @. There must be a record for each file opened. |
| 51 | An error has occurred while trying to open file — @. |
| 52 | The OWNER command will work with TAS-Professional 5.0 files only. |
| 53 | You have specified too many RELATEDs. The limit is 32 for all programs in the session. |
| 54 | You have specified too many menu choices; max is 25. |
| 55 | You have specified a key number for which there is no key. |
| 56 | You have not specified a SEARCH FILE value nor a file_number in this command. |
| 57 | You have not specified either a SEARCH FILE key number, nor a key expression in this command. |
| 58 | You must have a legal file_number for this command. |
| 59 | You can't delete records in non-TAS files — @ |
| 60 | The RAP buffer number specified was either 0 or more than the maximum allowed. |
| 61 | This file was not opened in a previous program — @ |
| 62 | The file being used has not been opened yet. |
| 63 | There are no fields named and this RESET_FLDS command will be ignored. |
| 64 | The matching field in the previous program field buffer was not found — @ |
| 65 | In this command you must specify the NUMBER of elements. |
| 66 | You have used an illegal type spec in the REDEFINE command. |
| 67 | An Alpha field must have a size specified in the REDEFINE command. |
| 68 | You have specified a handle number and there is no corresponding handle. |
| 69 | The program does not allow adding new items to this list; however you may browse it. |
| 70 | You are trying to change this list and there are not enough unused slots for the items needed. |
| 72 | You can't convert a TIME field to an INTEGER field. |
| 73 | You can't convert a DATE field to an INTEGER field. |
| 74 | You can't convert a POINTER field to an INTEGER field. |
| 75 | You can't convert a TIME field to a BYTE field. |
| 76 | You can't convert a DATE field to a BYTE field. |
| 77 | You can't convert a POINTER field to a BYTE field. |
| 78 | Internal err CRF |
| 79 | An error has occurred in BTRIEVE. |
| 82 | BTRIEVE error — @ |
| 83 | Press any key to continue. |
| 84 | Yes |
| 85 | No |
| 86–92 | Day names: Sunday / Monday / Tuesday / Wednesday / Thursday / Friday / Saturday |
| 93–104 | Month names: January / February / March / April / May / June / July / August / September / October / November / December |
| 105 | *** Invalid Date — Please Reenter *** |
| 106 | Save Record (Y/N) Y |
| 107 | Delete Record (Y/N) Y |
| 108 | Create File (Y/N) Y |
| 109 | The file you have tried to create already exists. If you 'CREATE' it again, all existing data will be LOST. Please change the file name or verify your actions. |
| 110 | Where do you want to print? (Screen/Printer/Disk) S |
| 111 | You must have a Buffer name for every non-TAS file — @ |
| 112 | You must specify a record size of every non-TAS file. |
| 113 | The maximum number of elements in an array to be sorted must be less than 32767. |
| 114 | The field in the FFLD() was not found in the field list. |
| 116 | The field in this command/expression must be of 'N' type. |
| 117 | You must MOUNT a Report Format before you can use the PRINT FORMAT command. |
| 118 | The Format number specified in the PRINT FORMAT LINE command is out of range or the format has not been MOUNTed. |
| 119 | The major field in an UPDATE ARRAY command must be in array form. |
| 120 | You have tried to use a field in an UPDATE ARRAY ADD/SUB command that is not an INTEGER type. |
| 121 | The only math allowed on pointers is add and subtract. |
| 122 | File: |
| 123 | An error has occurred while trying to open the print to file. Please check the file name. |
| 124 | The printer file already exists. Do you want to overwrite it? |
| 125 | The READ/WRITE commands may not be used with TAS Pro 5.0 files — @ |
| 126 | An error occurred while trying to set the position as required in this command. |
| 128 | The program has tried to open more files than are allowed. |
| 129 | An error has occurred while opening or reading the printer driver file. |
| 130 | The printer control command was not found. |
| 131 | The pointer field in this command must be of 'P' type. |
| 135 | An error has occurred while creating file — @ |
| 136 | **** BAD TIME — REINPUT **** |
| 137 | There is no space available in the Screen Field Buffer and another field is needed. Please increase the initial settings for this buffer. |
| 138 | The field in this command/function must be of D (date) type. |
| 139 | Records |
| 143 | You can't export to or import from a TAS Professional 5.0 file. |
| 144 | The program cannot find the import file specified in the command. |
| 145 | An error has occurred while attempting to open or write to the Export file. |
| 146 | The maximum size for an IMPORT/EXPORT record is 64k and you have exceeded this. |
| 147 | An error has occurred while trying to read a record from the Import file. |
| 148 | The field being passed and the associated receiving field in the PASS command must be the same type. |
| 149 | *** Bad Time — Reinput *** |
| 150 | Save the Record in File — @ |
| 151 | Delete the Record in File — @ |
| 152 | Are you sure you want to delete this line in the list? (Y/N) Y |
| 154 | An error occurred while opening or reading the ACS file as specified in the command. |
| 155 | The field provided is not large enough to hold the entire TRAP list as requested. |
| 156 | The search and array field types in the ALOC function must be of the same type. |
| 157 | The second field in the ALOC function must be an array field. |
| 158 | Where do you want to print? (Screen/Printer/Disk/List) S |
| 200 | Error during disk read/write. Btrieve — @ |
| 201 | Must open file before accessing it. Btrieve — @ |
| 202 | Tried to save a duplicate key when not allowed. Btrieve — @ |
| 203 | Changed keys and tried to do Next, Previous, etc. Btrieve — @ |
| 204 | Tried to modify a key value set as non-modifiable. Btrieve — @ |
| 205 | An error has occurred while trying to access/create/open the pre-image file required for the Transaction processing. |
| 206 | The disk is full. Btrieve — @ |
| 207 | A major (unrecoverable) error has occurred. Use your backups. |
| 208 | The file you have tried to open is not a standard TAS Professional file. It may be a damaged file. |
| 209 | Need to add the /T to the Btrieve trailer before the Transaction processing commands can be used. |
| 210 | You cannot nest Transactions. One has to be COMMITed before another can be started. |
| 211 | An error occurred during the Transaction process. You will need to roll back and restart. |
| 212 | You must have a Transaction Begin before a Transaction Rollback. |
| 213 | The maximum number of files that may be included in a Transaction is 12. You have exceeded it. |
| 214 | File is read-only; you cannot write or delete any records. Btrieve — @ |
| 215 | The number of buffers available has exceeded the number of files allowed by Btrieve. |
| 216 | The Owner is already set for the file. Btrieve — @ |
| 217 | The correct Owner name has not been provided for this file and it cannot be opened. |
| 218 | An error has been received by Btrieve from the Expanded Memory Manager. |
| 219 | This record has been changed by another user since you read it. |
| 220 | The lock table is full. Reset the /L option in the Btrieve load command. |
| 221 | The record you have tried to access has been deleted previously by another user. |
| 222 | All records that are updated/deleted within a Transaction must be locked before they can be changed. |
| 223 | The number of files you have tried to open is greater than the File specification in the Btrieve start-up command. |
| 225 | DOS is restricting access to this file/record. Btrieve — @ |
| 226 | This is not a TAS Professional 5.0 program. |
| 227 | This field is not indexed, or it has not been used within an ENTER or FIND command. You must use indexed fields in a SEARCH. |
| 228 | The file was not found in the list of opened files. |
| 229 | You have exceeded the maximum number of lines that can be wrapped in a print command. |
| 230 | The maximum number of WRAP'd fields in any one print line is 10. |
| 231 | You have specified a buffer for a non-TAS Btrieve file that is smaller than the record size of the file. |
| 232 | The maximum ENTER field size is 255 characters. |
| 233 | An error has occurred while attempting to compile an expression. |
| 234 | You have used too many internal screen buffers in this program. |
| 235 | You have tried to REDISPLAY a screen from an internal buffer and the buffer is empty. |
| 237 | You have tried to load a program that cannot fit in the space allocated for programs. |
| 238 | The Thru value in the PRINT FORMAT command is less than the last line # of the report format. |
| 239 | The printer is not operating. Output will default to the screen. |
| 240 | The printer number must be from 1 thru 3; program will default to printer 1. |
| 241 | You are trying to close a file that was opened in a previous program and cannot be closed here. |
| 242 | Only F type pointers are allowed in the FLIST option. |
| 243 | You have specified a file number value that is not legal. |
| 250 | Now is the time for all good men to come to the aid of … *(test string)* |
| 260 | ** No help message ** |
| 261 | You have specified an array field for the NMENU command and the array is out of range. |
| 262 | An error has occurred while trying to output to the printer. Do you want to continue? |
| 263 | You are trying to open a file without specifying the record size in the OPENV command. |
| 264 | You have tried to Execute a program and did not supply a name. |
| 265 | The record in file @ is locked by another user. |
| 266 | The record in file @ is locked by another user. Do you want to wait for it? |
| 267 | The number of active elements is greater than or equal to the number allocated. |
| 268 | The search reached the end of the file. |
| 269 | The search reached the beginning of the file. |
| 270 | The record was not found. |
| 271 | There are no records in the file. |
| 272 | There is no active record in the file so you cannot delete it. |
| 273 | Extra Memory Area numbers must be 1–4 only. |
| 274 | You have specified an Extra Memory Area number of 0. |
| 275 | The action you desire would exceed the size of the Extra Memory Area. |
| 276 | You may set the special file number to 1, 2, or 3 only. |
| 277 | The receiving offset field you have specified is not large enough to hold the result. |
| 278 | You have used too many internal trap buffers in this program. |
| 279 | You have tried to restore the TRAP table from an internal buffer but the buffer is empty. |
| 300 | Date sizes can be: |
| 301 | 5 (mm\yy) or 7 (mm\yyyy) or 8 (mm\dd\yy) or 10 (mm\dd\yyyy) |
| 302 | Time sizes can be: 5 (hh:mm) or 7 (hh:mm A) or 8 (hh:mm:ss) or 10 (hh:mm:ss A) or 11 (hh:mm:ss.00) or 13 (hh:mm:ss.00 A) |
| 306 | An ALPHANUMERIC field size may be from 1 through 65534 characters. |
| 307 | A NUMERIC field may be from 1 through 20 characters (includes decimal chars and sign). |
| 308 | A BYTE field size may be from 1 through 3 characters. |
| 309 | An INTEGER field size may be from 1 through 5 characters. |
| 310 | A RECORD field size may be from 1 through 10 characters. |
| 311 | *** DEMO VERSION *** There are more than 100 records in this file and the demo version is limited to 100. |
| 312 | Your copy of TAS Professional 5.0 hasn't been unlocked for the application described above. |
| 313 | This program requires the ADV50.OVL file to be loaded before it can be run. |
| 500 | The source file above was not found. Make sure the file has been placed in the proper subdirectory. |
| 501 | The Screen/Report format was not found. |
| 502 | The Screen/Report format file must not be larger than 64k. |
| 503 | There are no chars in the Screen/Report format file. |
| 504 | An error has occurred while reading the Screen/Report format file. |
| 505 | There is a programming error in the Screen/Report format file. |
| 506 | The number of field chars in the Screen/Report format line exceeds the limit. |
| 507 | There is a problem in a number for a portion of the Screen/Report format. |
| 508 | Screen field display color numbers must be constants from 1 through 7. |
| 510 | Color blocks (\C) are not allowed in Report formats. |
| 512 | The line is longer than 1024 characters, or the cr/lf pair was not found. |
| 513 | There has been an error discovered in the source file. |
| 514 | ** Compiling Program: @ |
| 515 | *** Compiling INCLUDE program: @ |
| 516 | *** COMPILER INTERRUPTED *** |
| 517 | An error occurred while trying to compile an external procedure. |
| 518 | Serious Errors have occurred during the compiling process. Please correct before using. |
| 519 | Warning Errors have occurred during the compiling process. The program has been saved but please correct. |
| 520 | Debug line generation ON |
| 521 | Debug line generation OFF |
| 522 | Display Procedure List ON |
| 523 | Display Procedure List OFF |
| 524 | The compiler was successful |
| 525 | Warning Error Messages will NOT appear |
| 526 | Changes have been made to the standard buffer sizes |
| 534 | The Command — @ is not a known TAS Professional 5.0 command. |
| 535 | *(see 534)* |
| 536 | All file handles available from DOS were in use. Please make sure you close files before opening more. |
| 537 | Access has been denied to you for the file requested. This means you do not have READ/WRITE privilege. |
| 538 | The path entered does not exist. |
| 539 | The program is unable to create the file above. Unknown reason. |
| 540 | There are no lines of code in the specified source file. |
| 541 | There was not enough space on the disk to save the run file. |
| 542 | The compiler was successful and the .RUN file has been created. |
| 545 | Quote marks are unbalanced in the line. |
| 546 | Syntax Error — @ |
| 547 | An unknown command modifier was found. |
| 548 | An unknown Compiler Directive was found. |
| 549 | An error was made in specifying the data type. The only choices are: A, B, D, F, I, N, P, R, T. |
| 550 | An unknown set option was specified. |
| 551 | The only choices for this set option are: On/Off or leave it blank. |
| 552 | The only choices for the Set Device option are: Screen or Printer. |
| 553 | Too many decimal characters have been specified in a constant. |
| 554 | An ELSE command has been found without a corresponding IF. |
| 555 | An ENDIF command has been found without a corresponding IF. |
| 556 | An ENDWHILE command has been found without a corresponding WHILE. |
| 557 | An EXIT command has been found without a corresponding WHILE. |
| 558 | A NEXT command has been found without a corresponding FOR. |
| 559 | A FLOOP command has been found without a corresponding FOR. |
| 560 | A FEXIT command has been found without a corresponding FOR. |
| 561 | A LOOP command has been found without a corresponding WHILE. |
| 562 | An ENDCASE cmd has been found without a corresponding SELECT. |
| 563 | There have been 1 or more IF cmds without corresponding ENDIF. |
| 564 | There have been 1 or more WHILE commands without corresponding ENDWHILE. |
| 565 | There have been 1 or more SELECT commands without corresponding ENDCASE. |
| 566 | There have been 1 or more FOR commands without corresponding NEXT. |
| 567 | The expression is too complex. Either increase the number of operators allowed or break it into separate expressions. |
| 568 | The end of the source file was encountered within a TEXT region. |
| 569 | The comparison type was not acceptable. |
| 570 | The parentheses are unbalanced in the expression. |
| 571 | There is an error in your expression. Probably a single numeric constant with no field specified. |
| 572 | The function in the expression is not a legal TAS Professional 5.0 function. |
| 573 | Memory field was not after the TO modifier. |
| 574 | You must have a receiving field in this command. |
| 575 | You must have a file name in this command. |
| 580 | You have specified too many #INCLUDE files in the program. Max is 10. |
| 581 | FILEDICT.B was not found. |
| 582 | FILELOC.B was not found. |
| 583 | FILEKNUM.B was not found. |
| 600 | The Code segment has grown larger than the memory allocated. |
| 601 | The Spec Code segment has grown larger than the memory allocated. |
| 602 | You have too many different named fields. |
| 603 | You have used too many different files. |
| 605 | You have reached the maximum nesting level for the IF command. |
| 606 | You have reached the maximum nesting level for the WHILE command. |
| 607 | You have reached the maximum nesting level for the SELECT/CASE command. |
| 608 | You have reached the maximum nesting level for the FOR command. |
| 609 | Warning: The field you are trying to add has already been added. |
| 610 | The maximum number of fields you may allocate is 2000. |
| 611 | You have tried to add more fields than you have allocated. |
| 612 | The field name specified was too long. Maximum 15 chars. |
| 613 | The field name is illegal. It must start with an alpha char from A–Z. |
| 614 | You have specified an unknown field type. The only acceptable types are A, B, D, F, I, N, P, R, T. |
| 615 | You must use a numeric constant for the field size. |
| 616 | You must use a numeric constant for the field decimal chars size. |
| 617 | You must use a numeric constant for the field array size. |
| 618 | Something is wrong with the array specifier. Please check it. |
| 619 | The field display size specified is too long for the field type. |
| 620 | You have not specified a field display size. |
| 621 | You cannot specify more than 8 decimal chars in a numeric field definition. |
| 622 | You have not specified a field name for this field. |
| 624 | This field was used in the program. It must be either DEFINEd or in the Data Dictionary. |
| 625 | You have defined a field that is also in the data dictionary. It will use the defined one and not the dictionary one. |
| 626 | You have tried to DEFINE too many fields at the same time. |
| 627 | The #XLATE compiler directive has been set in this program and the XLATE file was not found. |
| 628 | The key name was not found in FILEKNUM.B |
| 629 | The label name was used but was not set as a legal label. |
| 630 | The label name was already used. |
| 631 | The value in this instance must be a constant. |
| 632 | You can't specify a Pointer type constant. |
| 633 | You can't specify a Date type constant. Use =CTOD('date') instead. |
| 634 | You can't specify a Time type constant. Use =CTOT('time') instead. |
| 635 | An error has occurred in Btrieve. |
| 636 | The maximum size for any single source file is 64k. Split your program into smaller source files. |
| 637 | A library file is already open. You may open only one during compilation. |
| 638 | An error occurred while attempting to open the Library file specified. |
| 639 | An error occurred while accessing the Library file. |
| 641 | You may not use an expression or array field in a FIND (use SEARCH instead). |
| 642 | You must have the FD in this command. |
| 643 | There is a limit of 20 screen/report formats in a single program. |
| 645 | A label is required for this command. |
| 646 | You must have a format name in a MOUNT command. |
| 647 | The only legal format types are (S)creen and (R)eport. |
| 650 | The maximum number of nested functions is 10. |
| 651 | The screen/report format name used in the REMOUNT command hasn't been used in a MOUNT command. |
| 652 | There are 1 or more SCANS without ENDS. |
| 653 | The maximum number of nested SCANs is 20. |
| 654 | SEXIT without SCAN. |
| 655 | SLOOP without SCAN. |
| 656 | ENDS without SCAN. |
| 657 | You have exceeded the number of line labels specified for this program. |
| 658 | The value in the CASE command must be an integer numeric constant. |
| 659 | There is no START value for this FOR/NEXT loop and there must be one. |
| 660 | There is no STOP value for this FOR/NEXT loop and there must be one. |
| 661 | There is no STEP value for this FOR/NEXT loop and there must be one. |
| 662 | The Source Library Master file you have specified was not found. |
| 663 | The Defined Field Dictionary file (FILEDFLD) was not found. |
| 664 | The Source Library file (TASMSLB.B) was not found. This is required when compiling programs that use libraries. |
| 665 | A necessary source file was not found in the library for this program. |
| 666 | An error has occurred while attempting to open the Source Library. |
| 667 | A Screen/Report format with this name has already been found in this program. |
| 668 | The field used in the DUP option in the DEFINE command must have already been defined. |
| 669 | You have tried to initialize a Defined Field before all the DEFINE commands were done. |
| 670 | The maximum number of options in a standard TAS Pro 5.0 menu is 20. |

---

## Key observations

- **Errors 1–8** are startup errors; 1–4 are TAS Pro 5 era references (TASPRO.OVL, not tp7runtime.exe).
- **Error 35** contains a literal phone number (`919-932-3068`) — this was Computer Keyes (TAS Professional vendor) support.
- **Error 47/48** confirm `FILELOC.DBF` as a required runtime support file (file location registry).
- **Errors 82–104** double as UI strings: Btrieve error, day names (86–92), month names (93–104).
- **Errors 106–108** are user-prompt strings with default answers embedded.
- **Errors 200–232** are Btrieve-specific file I/O errors with full text descriptions.
- **Errors 265–266**: error 266 asks the user "Do you want to wait?" — confirms the TAS runtime has a record-lock retry dialog.
- **Errors 500–599** are compiler output messages; 514/515/640 use `@`/`\i` substitution placeholders.
- **Errors 581–583** confirm three mandatory runtime support files: `FILEDICT.B`, `FILELOC.B`, `FILEKNUM.B`.
- **Error 311** confirms a DEMO VERSION licensing check exists (≤100 records).
- **Error 312** confirms a product unlock/license check exists.

---

## Associated runtime support files

| File | Purpose (from error messages) |
|------|-------------------------------|
| `FILELOC.B` / `fileloc.dbf` | File location registry — maps file names to physical paths; required for OPENV |
| `FILEDICT.B` | Data Dictionary — field definitions; required at compile and runtime |
| `FILEKNUM.B` | Key number table — maps key names to key numbers |
| `FILEDFLD.B` | Defined Field Dictionary |
| `TASMSLB.B` | Source Library Master — required for library compilation |
| `ERRMSG.DBF` | This file — error message text table |
