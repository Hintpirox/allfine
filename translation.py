from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """**Hi {}**

I Am **All In Link Converter Bot** 🤖
👉I Will Convert **Mdisk Links** To Your **Linked Mdisk Api.**
👉I Will **shorten links** to your **favorite link Shortener.**
👉I Can Also Convert **Mdisk Link** To **Your** Linked Api And Then To Your **Linked Shortner Api.** 

👇 **UseFull Commands** 👇

💁‍♀️ Hit 👉 /help To Get Help.
➕ Hit 👉 /header To Get Help About Adding your **Custom Header Text** to bot.
➕ Hit 👉 /footer To Get Help About Adding your **Custom Footer** to bot.
🖼️ Hit 👉 /banner To Add **Banner** In **Photo**
👊Hit 👉 /Available_shortners To Get **Available Shortners List.**

Any Issue Contact - @CyniteSupport
"""

HELP_MESSAGE = """**Hey there! My name is {firstname} and I'm a link convertor and shortener bot here to make your work easier and help you earn more 💰.**

**I have a Lot Of features to help you out, such as:**

**• I can Convert any links or posts to your Linked Shortner Or Mdisk Api link. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)**

**• I Can auto add custom footer text to your every post. Hit 👉 /footer To know more...**

**• I Can auto add custom Header text to your every post. Hit 👉 /Header To know more...**

**• I Can replace / remove other's channel links with your channel link. Hit 👉 /Username To know More...**

**• I Can Automatically Replace Your *Banner Image To images in the post. Hit  👉/Banner To Know More...**

**• No need to share password or email to convert links.**

**Available commands:**

- **Send /Shortner To Connect Your Shortner Site**
- **Send /Shortner_api To Link Your Shortner Api**
- **Send /mdisk_api To Connect Your Mdisk Api**
- **/Info To Get Infomation About You**
- **/include_domain**
- **/exclude_domain**

Any Issue Contact - @CyniteSupport"""

ABOUT_TEXT = """
**Available Websites:**
    
Shortnerfly.com, 
droplink.co, 
gplinks.in, 
tnlink.in, 
za.gl, 
du-link.in, 
viplink.in, 
shorturllink.in, 
shareus.in, 
earnspace.in, 
mdisklink.link, 
mdiskshortner.link, 
pkin.me, 
try2link.com, 
adf.ly, 
bit.ly, 
shortly.xyz, 
tinyurl.com,
hypershort.com, 
theforyou.in, 
shorte.st, 
earn4link.in,
link.short2url.in, 
indianshortner.in
shortingly.me, 
open2get.in, 
dulink.in,
pdiskshortener.com, 
mdiskshortner.link,
bitshorten.com, 
rocklink.in, 
xpshort.com,
adrinolinks.in, 
linkbnao.com, 
linksxyz.in, 
short-jambo.com, 
ads.droplink.co.in, 
linkpays.in, 
pi-l.ink, 
link.tnlink.in, 
nanolinks.in
mdisk.me, 
Etc..
And more 🤩
"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

> `mslink` - Change all the links of the post to your MDisk account first and then short to {shortener} link.

> `shortener` - Short all the links of the post to {shortener} link directly.

> `mdisk` - Save all the links of the post to your Mdisk account.
    
To change method, choose it from the following options:
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Select Method", callback_data="method_command"),
            InlineKeyboardButton("Home", callback_data="start_command"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [InlineKeyboardButton("Close", callback_data="delete")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Select Method", callback_data="method_command"),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "MsLink", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "Shortener", callback_data="change_method#shortener"
            ),
            InlineKeyboardButton("Mdisk", callback_data="change_method#mdisk"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="start_command"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Back", callback_data="start_command")]]
)

USER_ABOUT_MESSAGE = """
**Here Is Your Information About You:**

**- 🤡 Shortener website: {base_site}**

**- ☑ Your Selected Method: {method}**

- 👾 Your Shortner API: {shortener_api}

- 📀 Mdisk API: {mdisk_api}

- 📎 Channel Username To Replace: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}
"""


MDISK_API_MESSAGE = """To add or update your Mdisk API, \n`/mdisk_api mdisk_api`
            
Ex: `/mdisk_api Qu7jX9V0Sn3q1JHdxjPp`
            
Others Mdisk Links will be automatically changed to the API of this Mdisk account

Get your Mdisk API from @VideoToolMoneyTree_bot

Current Linked Mdisk API: `{}`"""

SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 6LZq851sXofffPHugiKQq`

Linked Shortner Website: {base_site}

To change your Shortener Website: /site

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """📝 To set the header text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the header text, use the following command:

`/header remove`

This is a helpful way to add a consistent header to all of your messages. Enjoy! 🎉"""

FOOTER_MESSAGE = """📝 To set the footer text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the footer text, use the following command:

`/footer remove`

This is a helpful way to add a consistent footer to all of your messages. Enjoy! 🎉"""

USERNAME_TEXT = """Current username: {username}

To set the username that will be automatically replaced with other usernames in the post, use the following command:

`/username your_username`

__(Note: Do not include the @ symbol in your username.)__

To remove the current username, use the following command:

`/username remove`

This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎"""

BANNER_IMAGE = """
Usage: `/banner image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner remove`

Eg: `/banner https://telegra.ph/file/61a90c3d61fc457fa9ef5.jpg`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
