Attribute VB_Name = "Module1"
Sub kuhakukesuyo()

n = Cells(Rows.Count, "A").End(xlUp).Row
For i = 1 To n
    If Cells(n - i + 1, 1) = "" Or Cells(n - i + 1, 3) = "nan" Then
        Rows(n - i + 1).Delete

    End If
    
Next i


End Sub
