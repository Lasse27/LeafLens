# LeafLens

LeafLens ermöglicht es mithilfe von Machine Learning, Pflanzen auf Bildern zu erkennen. Die Anwendung wurde in Python entwickelt und basiert auf einer Flask-Anwendung, die im Backend Methoden aus OpenCV sowie Tensorflow oder PyTorch aufruft bzw. aufrufen soll.

<img src="https://github.com/user-attachments/assets/96bc5c73-2230-4412-aab4-7d3ee4716ab4" alt="Vorschaubild">

## Installation

### Für die Entwicklung

1. **Virtuelle Umgebung erstellen:**  
   Erstelle eine virtuelle Umgebung, um die Abhängigkeiten isoliert zu installieren.  
   ```bash
   python -m venv venv
   ```

2. **Abhängigkeiten installieren:**  
   Aktiviere die virtuelle Umgebung und installiere die benötigten Pakete aus der `requirements.txt`.  
   ```bash
   # Unter Windows
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

   (Weitere Anleitungen zur Einrichtung virtueller Umgebungen findest du im Internet.)

### Für den einfachen Gebrauch

Führe das bereitgestellte Python-Skript aus, welches automatisch Links auf dem Desktop und im Startmenü erstellt, über die du die Anwendung starten kannst.

## Nutzung

Die Anwendung verwendet intern das Modul **FlaskWebGUI**, welches die Flask-App in einem separaten Fenster anzeigt. Das Fenster ist simpel gehalten und enthält ein Drag-and-Drop-Feld, in das du das zu untersuchende Bild ziehen kannst. Nachdem ein Bild ausgewählt wurde, wird der Name der Pflanze automatisch am unteren Ende des Bildes angezeigt.

## Voraussetzungen

- **Betriebssystem:**  
  Das Programm wurde explizit für Windows entwickelt. Es kann nicht garantiert werden, dass die Anwendung auf Linux oder macOS ordnungsgemäß funktioniert.

- **Python:**  
  Es wird vorausgesetzt, dass Python bereits auf dem Rechner installiert ist. Falls nicht, muss Python erst installiert werden.

## Lizenz

LeafLens wird unter der [MIT-Lizenz](LICENSE) veröffentlicht.

## Mitwirken

Beiträge sind willkommen! Bei Interesse oder Fragen wende dich bitte an: **lassehillen@gmx.de**
