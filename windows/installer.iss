; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=Kodos
AppVerName=Kodos-2.1.1
AppPublisherURL=http://kodos.sourceforge.net
AppSupportURL=http://kodos.sourceforge.net
AppUpdatesURL=http://kodos.sourceforge.net
DefaultDirName={pf}\Kodos
DefaultGroupName=Kodos
AllowNoIcons=yes
LicenseFile=LICENSE.txt
OutputBaseFilename=kodos-2.1.1-installer

[Tasks]
; NOTE: The following entry contains English phrases ("Create a desktop icon" and "Additional icons"). You are free to translate them into another language if required.
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"
; NOTE: The following entry contains English phrases ("Create a Quick Launch icon" and "Additional icons"). You are free to translate them into another language if required.
Name: "quicklaunchicon"; Description: "Create a &Quick Launch icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "dist\kodos\Kodos.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Kodos\*.*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "help\*.*"; DestDir: "{app}\help"; Flags: ignoreversion recursesubdirs
Source: "screenshots\*.*"; DestDir: "{app}\screenshots"; Flags: ignoreversion recursesubdirs
Source: "images\*.*"; DestDir: "{app}\images"; Flags: ignoreversion recursesubdirs


; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[INI]
Filename: "{app}\Kodos.url"; Section: "InternetShortcut"; Key: "URL"; String: "http://kodos.sourceforge.net"

[Icons]
Name: "{group}\Kodos"; Filename: "{app}\Kodos.exe"
; NOTE: The following entry contains an English phrase ("on the Web"). You are free to translate it into another language if required.
Name: "{group}\Kodos on the Web"; Filename: "{app}\Kodos.url"
; NOTE: The following entry contains an English phrase ("Uninstall"). You are free to translate it into another language if required.
Name: "{group}\Uninstall Kodos"; Filename: "{uninstallexe}"
Name: "{userdesktop}\Kodos"; Filename: "{app}\Kodos.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Kodos"; Filename: "{app}\Kodos.exe"; Tasks: quicklaunchicon

[Run]
; NOTE: The following entry contains an English phrase ("Launch"). You are free to translate it into another language if required.
Filename: "{app}\Kodos.exe"; Description: "Launch Kodos"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{app}\Kodos.url"

