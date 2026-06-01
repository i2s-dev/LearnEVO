# Main Menu — Support Programs

Status: verified (text distilled from the vendor's help file).

*Source: EvoHELP.CHM → Main Menu (Support) Programs (3 CHM topics).*
*Extracted HTML in [samples/chm/extracted/](../../../samples/chm/extracted/).*

These three utilities appear on the EvoERP main menu Support section and assist with software maintenance and support. Two of them (Send Files and Send Screen Print) are outbound-communication tools that let users transmit data or screenshots directly to IS Tech Support for troubleshooting. The third (Check for Updates) queries the IS Tech Support website to determine whether the installed EvoERP version is current.

---

## Contents

- [Check for Updates](#check-for-updates)
- [Send Files](#send-files)
- [Send Screen Print](#send-screen-print)

---

## Check for Updates

*Source: [check_for_updates.htm](../../../samples/chm/extracted/check_for_updates.htm)*

### Purpose

This program checks the IS Tech Support website to see if you have the latest update installed and if patches are available for the update you are on.

### General Program Operation

When the program loads, the current version will be displayed and you will be advised whether you are on the latest major update and then whether patches are available for the version you are on. If updates are available, a list will identify the programs that are affected by the updates. You need to use **SM-V Check for and Install Updates** to actually download the updates.

---

## Send Files

*Source: [send_files.htm](../../../samples/chm/extracted/send_files.htm)*

### Purpose

This program simplifies the process of sending data files to IS Tech Support staff for the purpose of troubleshooting program problems that cannot be replicated with the test data they have.

### General Program Operation

The program loads listing all the data files in your company on the left side. A support representative will have told you what files are needed. Select those files and move them to the right side. Enter any additional text in the body of the email and attach any additional files requested.

Two send methods are available:

- **Send with Outlook** — if you use Outlook, click this button. This is the recommended method.
- **Send Email** — if you use a different email client, click this button and the email settings entered into Evo-ERP at **US-A Customize Settings** will be used. Note: if your email server requires a user login and password and you do not use Outlook, this program will not function properly. It may also not function properly for some other email servers.

### Security

The data files sent by this program are encrypted and cannot be viewed by anybody other than IS Tech Support staff who have the decryption program. IS Tech is willing to sign a Nondisclosure Agreement ensuring that any data provided will be used for troubleshooting purposes only. Even without a formal NDA, data is used solely for troubleshooting and is deleted once the issue is resolved.

---

## Send Screen Print

*Source: [send_screen_print.htm](../../../samples/chm/extracted/send_screen_print.htm)*

### Purpose

This program allows you to easily send tech support a screen print of a problem.

### General Program Operation

The program prompts you to close any non-Evo windows that you do not wish to share, then takes a screenshot and passes you to the same program opened by **Send Files** for you to enter the recipient email address.

---

## Cross-references

- **SM-V Check for and Install Updates** — the companion program that actually downloads and installs updates identified by Check for Updates. Check for Updates (this menu) only reports availability; SM-V performs the download.
- **US-A Customize Settings** — stores the email server settings used by Send Files when Outlook is not the email client.
- **Send Files** — Send Screen Print re-uses the Send Files interface for the email step; the two programs share that UI.
