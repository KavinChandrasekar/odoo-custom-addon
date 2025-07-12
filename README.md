# Custom Odoo Addon – Contact Enhancements

## 📌 Features
- Add custom field `Custom Code` to Contact
- Add `Follow-Up Date` and `Follow-Up Done` fields
- Daily cron job to auto-mark follow-up done if date matches today

## 🛠️ Installation
1. Copy this module into your Odoo addons path.
2. Go to Apps > Update Apps List.
3. Search for "Custom Odoo Addon" and install.

## 📋 Usage

### 🧩 Custom Code Field
- Go to **Contacts** → Open any contact.
- You will see a new field called **Custom Code** under the VAT field.

### ⏰ Follow-Up Automation (Cron Job)
- Add a **Follow-Up Date** to any contact.
- Each day, a **Scheduled Action** will:
  - Search for contacts with today's date
  - Auto-check the "Follow-Up Done" box
- You can also run the cron manually via:
  - **Settings → Technical → Automation → Scheduled Actions**

## 📅 Scheduled Job Details
| Name                | Auto Mark Follow-Up Done |
|---------------------|---------------------------|
| Model               | `res.partner`             |
| Method              | `_cron_check_followup_dates()` |
| Interval            | Every 1 day               |
| Condition           | `follow_up_date = today` and `follow_up_done = False` |
| Result              | Sets `follow_up_done = True` |

## 🔍 Screenshots
### custom field `Custom Code` to Contact
*
![screenshot-contacts-custom-field.png](static%2Fdescription%2Fscreenshot-contacts-custom-field.png)
![screenshot-custom-addon-app.png](static%2Fdescription%2Fscreenshot-custom-addon-app.png)
* 

### `Follow-Up Date` and `Follow-Up Done` fields
*
![ss-followup-fields.png](static%2Fdescription%2Fss-followup-fields.png)
![ss-scheduled-action-page.png](static%2Fdescription%2Fss-scheduled-action-page.png)
![ss-cronjob-run-manually.png](static%2Fdescription%2Fss-cronjob-run-manually.png)
![ss-cron-job-output.png](static%2Fdescription%2Fss-cron-job-output.png)
*

## 🧑‍💻 Author
[Kavin Chandrasekar](https://github.com/KavainChandrasekar)
