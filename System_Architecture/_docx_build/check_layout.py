from pathlib import Path
import json
import win32com.client

root=Path(__file__).resolve().parent.parent
path=root/'UAV_candidates_short_comparison.docx'
app=win32com.client.DispatchEx('Word.Application')
app.Visible=False
app.DisplayAlerts=0
doc=None
try:
 doc=app.Documents.Open(str(path),ConfirmConversions=False,ReadOnly=True,AddToRecentFiles=False)
 doc.Repaginate()
 print('PAGES',doc.ComputeStatistics(2),'PICTURES',doc.InlineShapes.Count,'TABLES',doc.Tables.Count)
 for i in range(1,doc.Tables.Count+1):
  table=doc.Tables(i)
  print('TABLE',i,'START_PAGE',table.Range.Information(3),'END_PAGE',doc.Range(table.Range.End-1,table.Range.End-1).Information(3))
 pdf=path.with_suffix('.pdf')
 doc.ExportAsFixedFormat(str(pdf),17)
 print('PDF',pdf)
 print('TEXT_LENGTH',len(doc.Content.Text))
finally:
 if doc is not None: doc.Close(False)
 app.Quit()
