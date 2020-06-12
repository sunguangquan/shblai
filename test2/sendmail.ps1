Set-Location $PSScriptRoot
 $config = import-csv 配置.CSV
 #电子邮件地址
$uname=$config.用户邮箱
#密码
$pwd=ConvertTo-SecureString  $config.用户密码  -AsPlainText -Force
$cred=New-Object System.Management.Automation.PSCredential($uname,$pwd)
#电子邮件地址
$SmtpServer = $uname -replace ".*@","smtp."

 #读取CSV文件
 #表格的格式是固定的，第一列必须是附件的文件名字,第二列是收件人，后面是任意列的抄送人。
 $content = cat user.csv
 $content = $content[1..$content.Length]
 #下面的是邮件类容，需要包含在引号里。
 $body = $config.内容

#下面的是邮件的主题
$Subject = $config.主题
#下面的是发件人
$from = $config.发送方



$pt = pwd

foreach($i in $content){
    $temp = $i.trim().split(",")
    $code = $temp[0]
    $fujian = @()
    $childits = Get-ChildItem $code
    if($childits){
    foreach($childit in $childits){
        $fujian1 = Join-Path -path $pt.Path -ChildPath $code
        $fujian += Join-Path -Path $fujian1  -ChildPath $childit.Name
        }
    }
    $cc = $temp[2..$temp.length] | Where-Object {$_}
    $to = $temp[1]
    $fujian
    #发送邮件

    Send-MailMessage -From $from -To $to  -Cc $cc -Attachments $fujian -Body $body -Subject $Subject -SmtpServer $SmtpServer -Credential $cred -Encoding "UTF8"  -BodyAsHtml
 }