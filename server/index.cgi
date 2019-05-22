#!/bin/bash
 
echo 'Content-type: text/html'
echo
nodeoption=`cat config.txt  |grep -Ev "^#" |grep -oE "^[^[:blank:]]{1,}"|awk '{print "<option  value=\""$1"\">"$1"</option>"}'`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" /><style type=\"text/css\">"
cat ./md.css
echo "</style><title>Looking Glass</title><head><body><h2>Looking Glass</h2>
<hr>
<form name=\"lg\" action=\"./lg.cgi\" method=\"get\">
<table>
<tr>
<td>节点</td>
<td>
<select name=\"node\">
$nodeoption
</select>
</td>
</tr>

<tr>
<td>域名</td>
<td><input type=\"text\" name=\"domain\" ></td>
</tr>
<tr>
<td>次数</td>
<td><input type=\"number\" name=\"t\" min=\"1\" max=\"5\" value=\"1\">(1-5)</td>
</tr>

<tr>
<td>使用IPv6</td>
<td>
<input name=\"ipv6\" type=\"checkbox\" value=\"ipv6\" />
</td>
</tr>


</table>
<input type=\"submit\" value=\"提交\">
<input type=\"reset\" value=\"重置\">
</form>
<hr>"
echo "`date` BASH $BASH_VERSION"
echo "
</body>
</html>
"