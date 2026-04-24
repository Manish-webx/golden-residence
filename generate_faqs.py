import re
import json

text = """1. What is Golden City Industrial Township?
Golden City Industrial Township is a comprehensively planned, 118.15-acre integrated industrial township located within IMT (Industrial Model Township) Manesar, Gurugram, Haryana. Developed by Worldwide Resort and Entertainment Pvt. Ltd. (Worldwide Realty), it offers freehold industrial plots across three blocks — A, B, and C — designed for manufacturing, logistics, warehousing, and investment. The township is RERA-registered, with 30–50% of plots already sold and possession underway.


2. Where is Golden City located?
Golden City is located in Sectors M9, M10, M13, and M14 of IMT Manesar, Gurugram, Haryana. It sits within the Delhi–Jaipur NH-48 corridor, approximately 18 km from Gurgaon city centre (Cyber City), 35 km from the Delhi border (Dhaula Kuan), and approximately 38 km from Indira Gandhi International Airport via NH-48. The Kundli–Manesar–Palwal (KMP) Expressway provides direct ring access to the wider NCR industrial belt.

3. Who is the developer / promoter of Golden City?
Golden City Industrial Township is developed and promoted by Worldwide Resort and Entertainment Pvt. Ltd., operating under the brand Worldwide Realty. The promoter is registered with HARERA (Haryana Real Estate Regulatory Authority) under RERA Registration No. 100 of 2022.

4. Is Golden City RERA registered?
Yes. Golden City Industrial Township is registered with HARERA — the Haryana Real Estate Regulatory Authority. RERA registration legally binds the developer to the project specifications and delivery timeline declared at registration, ensures buyer funds are protected in a designated escrow account, and gives buyers access to HARERA's grievance redressal mechanism. Verify the registration directly at haryanarera.gov.in.


5. What is the RERA registration number for Golden City?
The RERA registration number for Golden City Industrial Township is:
No. 100 of 2022 | Valid up to 29.09.2027
This single registration number applies across all blocks — A, B, and C. Verify at haryanarera.gov.in.


6. What types of plots are available in Golden City?
Golden City offers freehold industrial plots for a range of uses:
• Light and medium manufacturing (engineering, auto-ancillary, electronics, FMCG)
• Warehousing, logistics, and fulfilment facilities
• MSME factory units
• Investor-held industrial land
Plots carry an industrial land use designation under IMT Manesar planning norms on a DTCP/DGTCP-approved layout.


7. What are the plot sizes available in Blocks A, B, and C?
Block
Sectors
Plot Size Range
Block A
M9, M10
512 sq m to ~4.5 acres
Block B
M13
512 sq m to ~4.5 acres
Block C
M14
512 sq m to ~4.5 acres

Exact plot dimensions and current availability vary. Contact the sales team for an up-to-date inventory with precise measurements and block-wise layout.


8. Is this freehold or leasehold land?
Golden City plots are sold on freehold titles—you own the land outright, permanently. There is no annual ground rent, no lease renewal requirement, and no reversion of ownership to any authority at any point. Freehold title is freely transferable and can be mortgaged or used as collateral for business financing. A registered sale deed executed at the sub-registrar's office confirms your ownership.

9. What is the starting price per square yard?
Industrial plots at Golden City start from ₹4.84 Crores (for a 512 sq m plot at Base Selling Price + EDC/IDC charges, excluding GST). Pricing is tiered by plot size — larger plots benefit from a lower per-sq-m base rate. Premium Location Charges (PLC) apply for corner plots and wider road frontage. For a detailed price quote based on your preferred block and plot size, contact the sales team at +91 85100 00051 or goldenindustrialzone.com.


10. How many plots are still available?
Available inventory changes as bookings are confirmed. Contact the sales team directly for the most current availability by block and plot size. We recommend reaching out early — Golden City is an actively selling project with ongoing possessions underway.


11. Can I choose a specific plot location within the block?
Yes. The sales team will present the current inventory of available plots in each block, including their position on the block layout, dimensions, road frontage, and access. You can select your preferred plot based on your requirements—corner position, road frontage width, proximity to the main gate, or block preference. Your chosen plot is confirmed and reserved on payment of the booking amount.


12. Is Golden City HARERA approved?
Golden City Industrial Township is registered with HARERA — the Haryana Real Estate Regulatory Authority. The legally correct term is RERA registered (RERA registers projects; it does not issue an "approval"). Registration No. 100 of 2022, valid up to 29.09.2027. Verify at haryanarera.gov.in.

13. What is the RERA project ID?
RERA Registration Number: No. 100 of 2022
This can be used to look up the project on the HARERA portal at haryanarera.gov.in.


14. Who is the promoter registered with HARERA?
The promoter registered with HARERA is:
Worldwide Resort and Entertainment Pvt. Ltd. (Operating brand: Worldwide Realty)
This is the legal entity named in RERA registration No. 100 of 2022 and in all Agreement to Sell and Sale Deed documents. Ensure all your documents reflect this exact promoter name.



15. Is freehold title deed provided at registration?
Yes. Upon completion of payment per the agreed schedule, a registered Sale Deed is executed between the buyer and Worldwide Resort and Entertainment Pvt. Ltd. at the Sub-Registrar's office. This registered Sale Deed is your freehold title document. The process is:
1. Agreement to Sell (ATS) executed and registered
2. Payment completed per agreed schedule
3. Sale Deed executed and registered at Sub-Registrar's office
4. Mutation of land records in buyer's name with local authority
Upon registration, you hold legally valid, freehold title — the same ownership status as any immovable property in India.


16. What are the stamp duty and registration charges in Haryana?
Stamp duty and property registration charges in Haryana are levied by the State Government and are payable at the time of registering the Sale Deed at the Sub-Registrar's office. These charges are payable in addition to the plot purchase price. For the current applicable rates for industrial plot registration in Gurugram, we recommend consulting our sales team or a registered property lawyer, as rates are subject to government revision. Golden City's plot pricing does not include stamp duty or registration charges.


17. What is the possession date for Golden City industrial plots?
Possession of Golden City industrial plots is scheduled for the second half of 2026. Possession handover is underway. Individual plot possession schedules depend on the specific block and infrastructure completion progress for that plot. Buyers are notified of their individual possession schedule at the time of booking confirmation.


18. Has construction started?
Yes. Infrastructure development at Golden City is underway and at an active possession-commencement stage. Roads, boundary walls, power supply infrastructure, and drainage systems have progressed across the township. This is not a pre-launch, under-construction project — possession is actively being handed over per the RERA-registered handover schedule.


19. What infrastructure is included with the plot?
As a planned township, Golden City delivers township-level infrastructure with your plot:
• Internal roads: Wide, paved circulation roads designed for heavy vehicle movement (trucks, containers)
• Power supply: Industrial grid connection provision via dedicated industrial feeder
• Water supply: Industrial water connection provision
• Drainage: Storm water and planned effluent drainage network
• Perimeter security: Boundary wall enclosing the township
• Administration: Common admin and facility block
• Security: 24/7 manned security at main entry/exit points

20. Is the site accessible for visits currently?
Yes. Site visits can be arranged 7 days a week, 9:00 AM – 6:00 PM. The Golden City sales gallery is located at the project site in Sectors M9/M10/M13/M14, IMT Manesar, Gurugram. Visits are complimentary. We strongly encourage a site visit before booking — you can inspect the physical plot layout, completed infrastructure, and the surrounding IMT Manesar industrial environment first-hand. Contact the sales team to schedule your visit.

21. What amenities does the township provide?
Golden City's amenities are designed for operational and industrial efficiency:
• Wide internal roads (heavy-vehicle accessible throughout the township)
• Industrial power supply infrastructure
• Industrial water supply provision
• Planned storm water drainage
• 24/7 security at all entry and exit points
• Perimeter boundary wall (full township)
• Common administration block
The Golden City master plan also incorporates future commercial zone development, which is anticipated to add further long-term value for early industrial buyers as the township matures.


22. What is the booking process for a Golden City plot?
The buying process is straightforward and RERA-protected at every step:
1. Register your interest — call +91 85100 00051, WhatsApp +91 73534 56922, or submit the enquiry form on goldenindustrialzone.com; share your requirement (block, size, intended use)
2. Schedule a site visit — visit the township and review available inventory with a sales advisor
3. Select your plot — choose from current inventory across Blocks A, B, or C
4. Pay the booking amount — your selected plot is reserved and taken off the market
5. Agreement to Sell (ATS) — a registered ATS is executed, documenting the plot, price, and payment schedule; this is your primary legal document
6. Complete payment — as per the agreed schedule
7. Sale Deed & registration — freehold title registered in your name at the Sub-Registrar's office


23. What is the booking amount?
The booking amount required to reserve your plot is a proportion of the total plot cost. Contact the sales team for the current booking amount applicable to your selected block and plot size. Please note: under RERA, a promoter cannot accept more than 10% of the plot's cost as advance or application money before executing a registered agreement to sell.


24. Are there flexible payment plans?
Yes. Golden City offers flexible payment plans suited to different buyer profiles — manufacturer-buyers, logistics operators, investors, and institutional buyers. Payment plans can be structured around your acquisition timeline and financing requirements. Contact the sales team for a detailed payment schedule tailored to your plot selection.


25. What documents are required for booking?
Standard KYC and property purchase documents are required. Typically:
For individual buyers:
• Identity proof (Aadhaar / PAN / Passport)
• Address proof
• PAN card (mandatory for all property transactions)
For companies:
• Certificate of Incorporation
• Board Resolution authorising the purchase
• Company PAN
• Authorised signatory KYC
For NRI buyers: Additional OCI/passport documentation applies. Consult the sales team for the NRI-specific checklist.
The sales team will provide a complete, up-to-date document checklist at the time of booking confirmation.


26. How do I schedule a site visit?
Site visits are available 7 days a week. To schedule:
• Call or WhatsApp the sales team (contact details at goldenindustrialzone.com)
• Use the website form—submit the site visit request at goldenindustrialzone.com
• Walk in during business hours: 9:00 AM – 6:00 PM, any day
The sales gallery and project site are located at Golden City Industrial Township, Sectors M9/M10/M13/M14, IMT Manesar, Gurugram. Site visits are complimentary.


27. Is there a broker / referral programme?
Yes. Golden City works with registered channel partners and real estate brokers. If you are a property consultant or brokerage firm, contact the sales team to enquire about channel partner registration and referral arrangements. All channel partner transactions are formalized through proper agreements in compliance with RERA requirements.
"""

questions = []
for i in range(1, 28):
    questions.append(str(i) + "\. ")

# manually extract by finding each question
indices = []
for i in range(1, 28):
    q_str = f"{i}. "
    # find the index of this question only if it's at the start of a line
    match = re.search(f"(?m)^{q_str}", text)
    if match:
        indices.append((i, match.start()))

faqs = []
for idx in range(len(indices)):
    q_num, start_pos = indices[idx]
    end_pos = indices[idx+1][1] if idx + 1 < len(indices) else len(text)
    
    content = text[start_pos:end_pos].strip()
    lines = content.split('\n')
    
    question = lines[0].strip()
    # Ensure answer doesn't have empty paragraphs
    answer_parts = [line.strip() for line in lines[1:]]
    # Remove empty lines properly
    filtered_answer = []
    for line in answer_parts:
        if line != '':
            filtered_answer.append(line)
        else:
            filtered_answer.append('<br><br>')
    
    answer_html = ' '.join(filtered_answer).replace(' <br><br> ', '<br><br>').replace('<br><br> ', '<br><br>')
    
    faqs.append((question, answer_html))

html_output = ''
for i, (q, a) in enumerate(faqs):
    html_output += f'''        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)" id="faq-q{i+1}">
            {q}
            <i class="fas fa-plus"></i>
          </div>
          <div class="faq-answer">
            <p>{a}</p>
          </div>
        </div>\n'''

with open('faqs.html', 'w', encoding='utf-8') as f:
    f.write(html_output)
