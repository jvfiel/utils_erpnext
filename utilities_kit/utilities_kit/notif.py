import frappe
from datetime import timedelta


#dcl.dcl.notif.get_reminders
@frappe.whitelist()
def get_reminders(owner):
    msg = "Please be reminded of the following: "
    reminders = frappe.db.sql("""SELECT DISTINCT document_type, document_link FROM `tabDCL Reminders` WHERE owner=%s AND remind_in <= %s""",(owner,str(frappe.utils.get_datetime())))

    if reminders:
        for rem in reminders:
            try:
                msg += "<br>"+rem[0] + ": "+ rem[1]
            except:
                pass
        return msg
    else:
        return None

#dcl.dcl.notif.get_comments
@frappe.whitelist()
def get_comments(doc,method):
    # comms = frappe.db.sql("""SELECT * FROM `tabCommunication` WHERE communication_type='Comment' and comment_type='Comment' ORDER BY creation DESC LIMIT 2""",as_dict=True)
    # print(comms)
    # for com in comms:
    print ">>>>>>>>>>>"
    # print com
    print doc.content
    # print str(com['content']).replace(" ","")
    # if "remindme" in str(com['content']).replace(" ",""):
    #     print "remind me!"

    if doc.content:
        index = doc.content.find('/remindme')
        if index < 0:
            index = doc.content.find('/remind me')

        remind_type = ''

        index_end = doc.content.find('day')
        if index_end != -1:
            remind_type = 'Day'
        else:
            index_end = doc.content.find('hr')
            if index_end != -1:
                remind_type = 'Hr'


        print index,index_end, remind_type
        # message = com['content'].split(" ")
        # print message
        message = doc.content
        print message[index:index_end]
        message = message[index:index_end].split()

        day_or_hr = 0
        print message
        for mess in message:
            print mess
            try:
                day_or_hr = int(mess)
            except:
                pass

        print "day or hr", day_or_hr

        remind_in = frappe.utils.get_datetime()
        if remind_type == "Day":
            remind_in = remind_in + timedelta(days=day_or_hr)
        elif remind_type == "Hr":
            remind_in = remind_in + timedelta(hours=day_or_hr)

        dict = doc.as_dict()

        print dict

        remind = frappe.get_doc({"doctype":"DCL Reminders",
                                 "email":"",
                                 "owner":doc.owner,
                                 "document_link":doc.reference_name,
                                 "document_type":doc.reference_doctype,
                                 "remind_in":remind_in})
        remind.insert(ignore_permissions=True)