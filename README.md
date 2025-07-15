# Custom Odoo Addon – Contact Enhancements

## 📌 Features
- Add custom field `Custom Code` to Contact.
- Add `Follow-Up Date` and `Follow-Up Done` fields.
- Daily cron job to auto-mark follow-up done if date matches today.
- **Manual "Mark Follow-Up Done" smartbutton** added to each contact for manual control.

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
  - Search for contacts with today's date.
  - Auto-check the **"Follow-Up Done"** box.
- You can also run the cron manually via:
  - **Settings → Technical → Automation → Scheduled Actions**.

### 🔘 Manual "Mark Follow-Up Done" Smartbutton
- Go to **Contacts** → Open any contact.
- If **Follow-Up Done** is not yet checked:
  - A button labeled **"Mark Follow-Up"** will appear at the top.
  - Hovering over the button shows a tooltip:  
    **"Mark this Contact's Follow-Up as Done"**.
  - Clicking the button will immediately mark **Follow-Up Done** as True for that contact.
- This button disappears once the follow-up is completed.

> **Why?**  
> Use the button for manual control when follow-up is handled earlier than scheduled or when skipping automation.

## 📅 Scheduled Job Details

| Name                | Auto Mark Follow-Up Done |
|---------------------|---------------------------|
| Model               | `res.partner`             |
| Method              | `_cron_check_followup_dates()` |
| Interval            | Every 1 day               |
| Condition           | `follow_up_date = today` and `follow_up_done = False` |
| Result              | Sets `follow_up_done = True` |

## 🔍 Screenshots

### Custom Field `Custom Code` in Contacts
![screenshot-contacts-custom-field.png](static%2Fdescription%2Fscreenshot-contacts-custom-field.png)
![screenshot-custom-addon-app.png](static%2Fdescription%2Fscreenshot-custom-addon-app.png)

### Follow-Up Fields and Scheduled Actions
![ss-followup-fields.png](static%2Fdescription%2Fss-followup-fields.png)
![ss-scheduled-action-page.png](static%2Fdescription%2Fss-scheduled-action-page.png)
![ss-cronjob-run-manually.png](static%2Fdescription%2Fss-cronjob-run-manually.png)
![ss-cron-job-output.png](static%2Fdescription%2Fss-cron-job-output.png)

### Manual Smartbutton Example
![ss-after-mark-followup-done.png](static%2Fdescription%2Fss-after-mark-followup-done.png)
![ss-before-mark-followup-done.png](static%2Fdescription%2Fss-before-mark-followup-done.png)

## 🧑‍💻 Author
[Kavin Chandrasekar](https://github.com/KavainChandrasekar)
