""" Python Package Support """
# Not Applicable

""" Django Package Support """
# Not Applicable

""" Internal Package Support """
# Not Applicable

"""
 Support/choice_lists.py
 
 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2014-05-11
 Update by:   Matthew J Swann
 
 This file contains the set of choice lists for Project Knollgrass.
 
 These lists are organized alphabetically by name, not package.
 
 """

ASSIGNMENT_EXPEDIENCY = (
    ('0', 'Normal Assignment'),
    ('1', 'Rush Assignment')                 
)

ASSIGNMENT_FALLOUT = (
    ('0', 'Normal Assignment Completion'),
    ('1', 'Normal Cancelled Assignment'),
    ('2', 'Late Cancelled Assignment'),
    ('3', 'Client "no show"')
)

ASSIGNMENT_PAY_FREQ = (
    ('W', 'Weekly'),
    ('B', 'Bi-Weekly'),
    ('M', 'Monthly)'),
)

ASSIGNMENT_STATUS = (
    ('0', 'Unassigned'),
    ('1', 'Request Pending'),
    ('2', 'Confirmed Pending Interpreter'),
    ('3', 'Confirmed Assigned Interpreter'),
    ('4', 'Confirmed In-House Interpreter'),
    ('5', 'Completed'),                                
)

EVENT_REPEAT_INTERVALS = (
    (1, 'One week'),
    (2, 'Two weeks'),
    (3, 'Three weeks'),
    (4, 'One month'),
)

DAYS_OF_WEEK = (
    (1, 'M'),
    (2, 'T'),
    (3, 'W'),
    (4, 'R'),
    (5, 'F'),
    (6, 'S'),
    (7, 'S'),
)

EARLY_BIRD = (
     ('1', 'One Week'),
     ('2', 'Two Weeks'),
     ('3', 'Four Weeks')                       
)

ENITY_GENERAL_TYPES = (
    ('G', 'Government'),
    ('E', 'Education'),
    ('L', 'Legal-Court'),
    ('M', 'Medical'),
)

ENTITY_TYPES = (
    ('G-CN', 'Conference'),
    ('G-CO', 'Corporate'),
    ('G-GV', 'Government'),
    ('G-PE', 'Performance'),
    ('G-RS', 'Retail & Service'),
    ('G-NP', 'Non-Profit'),                 
    ('E-PR', 'Primary'),
    ('E-SE', 'Secondary'),
    ('E-HS', 'Higher : S.T.E.M.'),
    ('E-HL', 'Higher : Liberal Arts'),           
    ('L-AF', 'Attorney Firm'),
    ('L-CT', 'Court'),            
    ('M-DT', 'Dental & Vision'),
    ('M-HO', 'Hospital'),
    ('M-MH', 'Mental Health'),
    ('M-PC', 'Primary Care'),
    ('M-SP', 'Specialty Care'),    
    ('M-VM', 'Veterinary Medicine'),
        )

ENTITY_TYPES_VERBOSE = (
    ('G-CN', 'Government - Conference'),
    ('G-CO', 'Government - Corporate'),
    ('G-GV', 'Government - Government'),
    ('G-PE', 'Government - Performance'),
    ('G-RS', 'Government - Retail & Service'),
    ('G-NP', 'Government - Non-Profit'),                 
    ('E-PR', 'Education - Primary'),
    ('E-SE', 'Education - Secondary'),
    ('E-HS', 'Education - Higher : S.T.E.M.'),
    ('E-HL', 'Education - Higher : Liberal Arts'),           
    ('L-AF', 'Legal - Attorney Firm'),
    ('L-CT', 'Legal - Court'),            
    ('M-DT', 'Medical - Dental & Vision'),
    ('M-HO', 'Medical - Hospital'),
    ('M-MH', 'Medical - Mental Health'),
    ('M-PC', 'Medical - Primary Care'),
    ('M-SP', 'Medical - Specialty Care'),    
    ('M-VM', 'Medical - Veterinary Medicine'),
        )

EVENT_ATTIRE = (
    ('B', 'Business'),
    ('C', 'Casual'),
    ('F', 'Formal'),
    ('R', 'Rugged'),
    ('X', 'Business Casual')        
)

GENDER = (
    ('X', 'Undisclosed'),
    ('F', 'Female'),
    ('M', 'Male'), 
)

LANGAUGE_PREFERENCES = (

)

GENDER_PREFERENCES = (
    ('X', 'No gender preference'),
    ('F', 'Female preferred'),
    ('M', 'Male preferred'), 
)
 

KNOLL_TYPES = (
    #('IND', 'Individual'),
    ('BUS', 'Business'),
    ('ICO', 'Interpreting Company'),
)

LATE_CANCEL = (
    ('1', '24 Hours'),
    ('2', '48 Hours'),
    ('3', '72 Hours')              
)

MINIMUM_ONSITE = (
    ('0', 'No Minimum Time'),
    ('1', '30 Minutes'),
    ('2', 'One Hour'),
    ('3', 'Two Hours')      
) 

MINIMUM_REMOTE = (
    ('0', 'No Minimum Time'),
    ('1', '5 Minutes'),
    ('2', '15 Minutes'),
    ('3', '30 Minutes')      
) 

PAYMENT_METHODS = (
    ('S', 'Stripe'),
    ('D', 'Dwolla'),
    ('M', 'Manual Payment'),
    ('N', 'if run recursive knoll_tag'),
)

PAID_STATUS = (
    ('B', 'Pro-Bono'),
    ('C', 'Contested'),
    ('P', 'Paid'),
    ('U', 'Un-Paid')
)

PARTICIPANT_DESIGNATIONS = (
    ('S', 'Staff Participant {in-house}'),
    ('M', 'Medical Aide'),
    ('O', 'Outside Participant'),
    ('G', 'Municipal Escort')
)

PERMISSIONS = (
    ('1', 'Member'),
    ('2', 'Coordinator'),
    ('3', 'Admin')
)

PLAN_GROUPS = (
    ('B', 'Business'),
    ('I', 'Interpreting Company'),
)

RUSH_SCHEDULE = (
    ('1', '24 Hours'),
    ('2', '48 Hours'),
    ('3', '72 Hours'),             
) 

SCHEDULE_DESIGNATIONS = (
    ('A', 'Available'),
    ('U', 'Unavailable'),                  
    ('N', 'Non-Working Hours'),               
)

STATEMENT_TYPE = (
    ('A', 'Assignment Statement'),
    ('S', 'Subscription Statement'),
)

SUBSCRIPTION_PAY_FREQ = (
    ('M', 'Monthly'),
    ('Y', 'Yearly'),
)

TZ_LIST = (
        ('US/Alaska'),
        ('US/Aleutian'),
        ('US/Arizona'),
        ('US/Central'),
        ('US/East-Indiana'),
        ('US/Eastern'),
        ('US/Hawaii'),
        ('US/Indiana-Starke'),
        ('US/Michigan'),
        ('US/Mountain'),
        ('US/Pacific'),
        ('US/Pacific-New'),
        ('US/Samoa')
    )

USER_TYPES = (
    ('person', 'Person'),
    ('interpreter', 'Interpreter'),
)

US_STATES = ( 
    ('AL', 'Alabama'), 
    ('AK', 'Alaska'), 
    ('AZ', 'Arizona'), 
    ('AR', 'Arkansas'), 
    ('CA', 'California'), 
    ('CO', 'Colorado'), 
    ('CT', 'Connecticut'), 
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'), 
    ('FL', 'Florida'), 
    ('GA', 'Georgia'), 
    ('HI', 'Hawaii'), 
    ('ID', 'Idaho'), 
    ('IL', 'Illinois'), 
    ('IN', 'Indiana'), 
    ('IA', 'Iowa'), 
    ('KS', 'Kansas'), 
    ('KY', 'Kentucky'), 
    ('LA', 'Louisiana'), 
    ('ME', 'Maine'), 
    ('MD', 'Maryland'), 
    ('MA', 'Massachusetts'), 
    ('MI', 'Michigan'), 
    ('MN', 'Minnesota'), 
    ('MS', 'Mississippi'), 
    ('MO', 'Missouri'), 
    ('MT', 'Montana'), 
    ('NE', 'Nebraska'), 
    ('NV', 'Nevada'), 
    ('NH', 'New Hampshire'), 
    ('NJ', 'New Jersey'), 
    ('NM', 'New Mexico'), 
    ('NY', 'New York'), 
    ('NC', 'North Carolina'), 
    ('ND', 'North Dakota'), 
    ('OH', 'Ohio'), 
    ('OK', 'Oklahoma'), 
    ('OR', 'Oregon'), 
    ('PA', 'Pennsylvania'), 
    ('RI', 'Rhode Island'), 
    ('SC', 'South Carolina'), 
    ('SD', 'South Dakota'), 
    ('TN', 'Tennessee'), 
    ('TX', 'Texas'), 
    ('UT', 'Utah'), 
    ('VT', 'Vermont'), 
    ('VA', 'Virginia'), 
    ('WA', 'Washington'), 
    ('WV', 'West Virginia'), 
    ('WI', 'Wisconsin'), 
    ('WY', 'Wyoming')
         )
