#!/bin/bash
 
echo 'Content-type: text/html'
echo
query="$QUERY_STRING&"
node=`echo "$query" | ./query.sh node`
domain=`echo "$query" |./query.sh domain| grep -E -o "([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?)|(((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))))"|head -1`
t=`echo "$query" |./query.sh t| grep -E -o "[1-5]{1}"|head -1`
ipv6=`echo "$query" |./query.sh ipv6 |head -1`
nodestr=`cat config.txt|grep "^${node} "|head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" /><style type=\"text/css\">
"
cat ./md.css

if [[ "$node" == "" ]] || [[ "$node" == "null" ]] || [[ "$nodestr" == "" ]]
then
echo "</style><title>Looking Glass</title><head><body><h2>Looking Glass</h2>
<hr>
<pre>
错误:   节点为空或不存在
</pre>
<hr>
`date` BASH $BASH_VERSION

</body>
</html>
"


else
eval set -- $nodestr
nodeurl="$3"
echo "</style><title>Looking Glass</title><head><body><h2>Looking Glass - 节点 $node</h2>
<hr>
<pre>
正在请求节点API请等待..."
curl $2 "${nodeurl}?domain=${domain}&t=${t}&ipv6=${ipv6}"
echo "
</pre>
<hr>
`date` BASH $BASH_VERSION

</body>
</html>
"
fi