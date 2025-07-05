# odoo-custom-addon

This is a simple **custom Odoo15 module** that extends the core `res.partner` (Contacts) model by adding a custom field called **Custom Code**.

It's built as clean, real-world example of how to:
 - Extend existing Odoo models (`_inherit`)
 - Use XML views with `inherit_id` and `xpath`

## Feature
 - Adds a new `x_custom_code` char field to Contacts.
 - Displays the field directly **below the Tax ID** on the Contact form.
 - Uses clean XML view inheritance - no core hacks.
 - Packaged as reusable, installable Odoo module.

## How to Use
1. Clone or copy this module into your `custom_addons` folder.
2. Make sure `custom_addons` in included in your `addons_path` in odoo.conf:    addons_path = E:\odoo\odoo-15.0\odoo\addons,E:\odoo\odoo-15.0\addons,E:\odoo\odoo-15.0\custom_addons
3. Restart Odoo and Update the Apps List in Developer Mode.
4. Search for odoo custom addon or Custom CRM Feature in Apps.
5. Install the module.
6. Open any Contact - you'll see the Custom Code field under the Tax ID.

### **How this Odoo Addon Works**
* **Models:** Python class define the database structure.
 This module inherits Odoo's built res.partner model and adds the x_custom_code field.
* **Vievs:** XML files control the user interface.
  The module inherits the exisitng Contact form view and inserts the new field exactly where needed using an xpath targeting the Tax ID.
* **ORM:** Odoo's ORM means you work in Python and let Odoo handle the SQL behind the scenes.
* **Inheritance:** Instead of editing core fiels, you inherit models and views safely. This keeps upgrades and maintainance clean.
* **Security:** An ir.model.access.csv file ensures users have the right permissions to read/write the new field.


### Screenshots
Below are real screenshots showing the module in action:
Installed Custom App: ![screenshot-contacts-custom-field.png](static%2Fdescription%2Fscreenshot-contacts-custom-field.png)
Custom Code Field on Contact Form: ![screenshot-custom-addon-app.png](static%2Fdescription%2Fscreenshot-custom-addon-app.png)

# Author
Kavin Chandrasekar
[GitHub](https://github.com/KavinChandrasekar)

### For New Developers
* Odoo models, fields and the ORM
* XML views with inherit_id + xpath
* How to extend core ERP features cleanly
* Good Git & folder structure for custom addons

### Next Step
* Try Adding another field or report.
* build a workflow custom addon.
