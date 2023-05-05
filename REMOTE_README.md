# Remote tutorial

## Requisites

- [Google Sheets](https://sheets.google.com/)
- [This plugin for sheets](https://workspace.google.com/marketplace/app/webhooks_for_sheets/860288437469), developed by [Sourabh Choraria](https://script.gs/)
- [Canary Tokens](https://canarytokens.org/generate)
  
## Tutorial (setup sheets)
*If anything is unclear, going to the actual [documentation page](https://script.gs/webhooks-for-sheets/) might clear things up.*

Download the plugin and accept the Terms and Conditions.

Open a new Google Sheet but don't edit anything into it yet.  
At the bottom right of the sheet, a little arrow must be clicked to open the sidebar. This bar will now contain a new icon called "WebHook for sheets".  
![](https://script.gs/content/images/size/w1000/2022/04/Screenshot-2022-04-09-at-20.35.35.png)

Press "enable" and scroll down to "refresh". After the sheet refreshed, go back to the icon and select the sheet you want to use. In this case, I used "sheet 1". After everything is correctly configured, press "create".

![](https://script.gs/content/images/size/w1000/2022/04/Screenshot-2022-04-09-at-20.35.52.png)

On the next screen, press "enable" and next
![](https://script.gs/content/images/size/w1000/2022/04/Screenshot-2022-04-09-at-20.36.32.png)

Manually reload the sheet and a new "WebHooks" button will appear and the lint above, press "Authorize"
![](https://script.gs/content/images/size/w1000/2022/04/Screenshot-2022-04-09-at-20.37.30.png).

After yet *another* reload, going to the right "WebHook" icon the actual webhook link will appear (copy this one).

## Tutorial (canarytokens)
Select your preffered token and paste the webhook link recieved from the plugin. A "note" can be added so you can see which token was accessed at a glance.

Accessing any of the tokens will generate a new line in the selected sheet from one of the first steps in the sheets tutorial.

## Tutorial (overview)
It might be handy to have a little overview of newly created tokensn and if they have been accessed.   
For this, create a new "page" in the currently existing sheet and use the following code excerpts:

Newly created / total amount of tokens generated:  
`=COUNTIF(Sheet1!C:C;"Congrats! The newly saved webhook works")`

Amount of alerted tokens:  
`=COUNTIF(Sheet1!C2:C100;"<>Congrats! The newly saved webhook works";Sheet1!C2:C100;"<>")`

These might have to be tweaked based on at which line your tokens start.