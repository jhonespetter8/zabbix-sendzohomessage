Script submit message to Zoho Cliq
=====
> Created for use in Zabbix

Documentation Zoho
=====
- [Documentation Zoho for post message using cli](https://help.zoho.com/portal/en/community/topic/cliq-bots-post-message-to-a%C2%A0bot-using-the-command-line)
- [Generate token Zoho](https://accounts.zoho.com/apiauthtoken/create?SCOPE=ZohoCliq/InternalAPI)
- [Generate model message](https://cliq.zoho.com/messagebuilder)


Requirements for code
=====
<pre><code>
pip install --upgrade pip
pip install requirements.txt
</pre></code>

Usage
=====

Add token in variable
<pre><code>
token="YOURTOKEN"
</pre></code>

Execute script
> DESTINATION is name for channel or bot
<pre><code>
./sendzohomessage.py "DESTINATION" "SUBJECT" "MESSAGE" 
</pre></code>
