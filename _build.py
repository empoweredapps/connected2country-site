#!/usr/bin/env python3
"""Connected2Country static site builder. Edit the data below, run `python3 _build.py`, upload out/ to public_html."""
import os, shutil, json, html
from datetime import date

OUT = "out"
BASE = "https://connected2country.au"
BRAND = "Connected2Country"
PHONE = "0438 805 294"; PHONE_INTL = "+61438805294"; EMAIL = "helen@connected2country.au"
ABN = "23 319 539 776"
TODAY = date.today().isoformat()

# ------------------------------------------------------------------ content
SERVICES = [
 dict(slug="traditional-owner-consultation", nav="Traditional Owner consultation",
  title="Traditional Owner Consultation Darwin NT | Anthropologist-led",
  h1="Traditional Owner and Native Title holder consultation",
  desc="Anthropologist-led consultation with Larrakia and other Traditional Owners for developments in Darwin, Palmerston and the Top End. Right people, proper process, defensible consent records for your approval.",
  intro="Consultation with Traditional Owners and Native Title holders is the foundation of most heritage, sacred site, planning and environmental approvals in the Northern Territory. Connected2Country identifies the right people to speak for Country, designs a culturally appropriate process, runs meetings and on-Country visits, and records outcomes in a form regulators, land councils and lawyers accept.",
  bullets=["Identification of Traditional Owners, custodians and Native Title holders for the project area, drawing on land council, AAPA, Native Title and published anthropological records",
           "Consultation design: who, where, in what order, with what information, and how consent or objection is recorded",
           "Facilitation of meetings, on-Country site visits and family-group discussions, with interpreters and cultural advisers where needed",
           "Consultation registers, meeting records, consent and conditions documentation suitable for EIS, AAPA, Heritage Branch and Development Consent Authority submissions",
           "Ongoing liaison through construction, including cultural monitors and incident response",
           "Advice on engagement under the Aboriginal Land Rights (Northern Territory) Act 1976, the Native Title Act 1993 and land council processes"],
  who="Developers, civil head contractors and project managers with a Darwin or Top End project that needs Traditional Owner input; heritage and environmental consultancies that need a Darwin-based anthropologist for the consultation component; NT Government agencies, Defence contractors and utilities.",
  pricing="Scoped and quoted before work starts. Defined consultation programs are fixed price; open-ended engagement is on an agreed day rate with meeting payments and interpreter costs at cost.",
  faqs=[("Who are the Traditional Owners for Darwin?","The Larrakia people are the recognised Traditional Owners of the Darwin region, including Darwin, Palmerston and much of the rural area. Who speaks for a specific place within Larrakia country, and for places on the margins of neighbouring estates, is a matter for proper anthropological inquiry rather than a single list, which is what the consultation process establishes."),
        ("Is Traditional Owner consultation legally required?","It depends on the approval pathway. AAPA Authority Certificates are issued on the basis of consultation with custodians; works on Aboriginal land require land council and Traditional Owner consent under the Land Rights Act; NT EPA assessments and Development Consent Authority processes expect it; and Native Title future act processes require notification or negotiation. Even where it is not a formal requirement, documented consultation is the single best protection against delay later."),
        ("How long does consultation take?","Allow six to twelve weeks for a typical Darwin development, longer for remote communities or where sorry business, ceremony or the Wet season affects availability. Early engagement is the only reliable way to shorten the critical path.")]),
 dict(slug="aapa-authority-certificate-sacred-sites", nav="AAPA certificates & sacred sites",
  title="AAPA Authority Certificate Support & Sacred Site Advice NT",
  h1="AAPA Authority Certificate support and sacred site advice",
  desc="Help obtaining and complying with Aboriginal Areas Protection Authority (AAPA) Authority Certificates in the NT: applications, custodian consultation, restricted work area interpretation and construction compliance.",
  intro="An Authority Certificate from the Aboriginal Areas Protection Authority is the only legal protection against prosecution under the Northern Territory Aboriginal Sacred Sites Act 1989. Connected2Country has worked on sacred site surveys with AAPA and custodians from both the land council and the proponent side, and helps proponents get the certificate, understand its conditions and stay compliant on site.",
  bullets=["Pre-application advice: whether a certificate is needed, what area to apply over and how to describe the works to avoid re-applications",
           "Desktop review of AAPA register abstracts, previous certificates and anthropological literature for the project area",
           "Support to custodian consultation and sacred site surveys, including attendance on Country",
           "Plain-English interpretation of Authority Certificate conditions, restricted work areas and buffers for engineers and site supervisors",
           "Sacred site awareness inductions, site marking protocols and compliance inspections during construction",
           "Advice on variations, amendments and incidents, and on registering sites where custodians request it"],
  who="Developers and contractors applying for or working under an Authority Certificate in Darwin, Palmerston, the rural area and across the NT; environmental consultants preparing EIS culture and heritage chapters; NT Government and Defence project teams.",
  pricing="Pre-application advice and desktop reviews are fixed price. Consultation support and construction compliance are on an agreed day rate.",
  faqs=[("Do I need an AAPA Authority Certificate for my development?","If your works could affect a sacred site, a certificate is the only way to be sure you are protected. In practice, most subdivisions, infrastructure projects and works near the coast, waterways, rock outcrops or significant trees in the Darwin region apply for one. AAPA charges fees based on project value; we can advise before you apply whether the application is worth it and how to scope it."),
        ("What is a restricted work area?","A restricted work area (RWA) is an area defined in an Authority Certificate within which particular works are prohibited or conditioned to protect a sacred site. Conditions commonly limit ground disturbance, vegetation clearing, access or vehicle movement. The site itself is confidential; the RWA is what the proponent must manage."),
        ("Can Connected2Country issue a sacred site clearance?","No. Only AAPA issues Authority Certificates. Connected2Country prepares you for the application, supports the custodian consultation and helps you comply with the conditions.")]),
 dict(slug="cultural-heritage-assessment", nav="Cultural heritage assessment", img="heritage-plateau.jpg", img_alt="Landsat satellite image of dissected sandstone plateau country, rendered in ochre tones", credit="Imagery: NASA/USGS Landsat (public domain)",
  title="Cultural Heritage & Cultural Values Assessment Darwin NT",
  h1="Cultural heritage and cultural values assessments",
  desc="Ethnographic and cultural values assessments, Heritage Act 2011 advice and EIS culture and heritage chapters for projects in Darwin, the Top End and the NT, prepared by an anthropologist and archaeologist.",
  intro="Cultural heritage is more than archaeological sites. Connected2Country assesses the intangible, living and historical values that Aboriginal people hold for a place, alongside the tangible heritage protected under the Heritage Act 2011 (NT), and presents them in a form that planners, assessors and courts can use.",
  bullets=["Desktop cultural heritage assessments: register searches, literature review, previous surveys and constraints mapping",
           "Ethnographic and cultural values assessments with Traditional Owners, including intangible values, story, kinship and ecological knowledge",
           "Archaeological survey coordination and field recording, with specialist archaeologists engaged for larger programs",
           "Culture and heritage chapters for NT EPA environmental impact statements and referrals",
           "Heritage Act 2011 advice: declared places, heritage significance, works approvals and Heritage Council submissions",
           "Ethno-ecology research linking cultural values to flora, fauna, water and seasonal use"],
  who="Proponents of subdivisions, infrastructure, Defence, energy and resource projects; environmental consultancies that need the heritage component delivered locally; land councils and Aboriginal corporations documenting values on their own Country.",
  pricing="Desktop assessments are fixed price. Field assessments are quoted on area, access and number of Traditional Owner participants.",
  faqs=[("What is the difference between the Heritage Act and the Sacred Sites Act?","The Heritage Act 2011 (NT) protects declared heritage places and objects, plus all Aboriginal and Macassan archaeological places and objects, and is administered by the Heritage Branch. The Northern Territory Aboriginal Sacred Sites Act 1989 protects sacred sites, which are places of significance under Aboriginal tradition, and is administered by AAPA. A project often needs to deal with both."),
        ("Do you do archaeology as well as anthropology?","Yes. Helen Haritos holds an honours degree in archaeology and has conducted archaeological surveys in the NT, and partners with specialist archaeologists for larger programs. Most Top End projects need both disciplines working together."),
        ("Can the assessment be used in an EIS?","Yes. Assessments are written to NT EPA environmental factor guidance for culture and heritage and are structured so they drop straight into an EIS or referral.")]),
 dict(slug="cultural-heritage-management-plans", nav="Heritage management plans",
  title="Cultural Heritage Management Plans & CEMP Heritage Sections NT",
  h1="Cultural Heritage Management Plans and CEMP heritage sections",
  desc="Project-specific Cultural Heritage Management Plans (CHMPs) and the cultural heritage sections of Construction Environmental Management Plans for NT civil and development projects, with inductions, monitoring and inspections.",
  intro="Approvals come with conditions and the conditions have to be lived with for the life of the project. Connected2Country writes management plans that construction crews can actually follow, then provides the inductions, monitoring and inspections that show the conditions were met.",
  bullets=["Cultural Heritage Management Plans tied to Authority Certificate conditions, Heritage Act approvals and Traditional Owner agreements",
           "Cultural heritage sections and procedures for Construction Environmental Management Plans",
           "Unexpected finds and ancestral remains procedures",
           "Site induction content and delivery for crews and subcontractors",
           "Cultural monitor programs with Traditional Owners during ground disturbance",
           "Compliance inspections, audits and close-out reporting for superintendents and regulators"],
  who="Civil head contractors and subcontractors on NT Government, Defence, utility and private development contracts; developers passing approval conditions down to contractors; environmental consultants preparing CEMPs who need the heritage component.",
  pricing="Plans are fixed price for defined scopes. Inductions, monitoring and inspections are on an agreed day rate or per-visit price.",
  faqs=[("Does my CEMP need a cultural heritage section?","Almost always. NT Government, Defence and most private contract environmental clauses require the CEMP to address heritage and sacred sites, and any Authority Certificate or Heritage Act condition has to be translated into site controls. A generic paragraph will not satisfy a superintendent."),
        ("What happens if we find artefacts or remains during works?","Stop work in the immediate area, protect the find and notify the Heritage Branch (and police for suspected human remains). Your plan should say exactly who does what. Connected2Country responds to unexpected finds across the Darwin region and advises remotely elsewhere."),
        ("Can you work with our existing environmental consultant?","Yes. Connected2Country regularly provides the heritage component to environmental consultancies, including Bell Enviro, so that one integrated plan goes to the client.")]),
 dict(slug="anthropological-research-expert-reports", nav="Research & expert reports",
  title="Anthropological Research, Native Title & Expert Reports NT",
  h1="Anthropological research, native title support and expert reports",
  desc="Consultant anthropologist for native title and land claim research, genealogies, connection reports, land council and ALRA matters and expert reports in the Northern Territory and East Kimberley.",
  intro="Over 20 years in Aboriginal land, heritage and native title work in the Northern Territory, including senior anthropologist roles with the Northern Land Council and the Tiwi Land Council, plus ANU-CNTA native title research training, underpin a research practice that land councils, Aboriginal corporations, lawyers and government can rely on.",
  bullets=["Native title connection research, genealogies and claim group descriptions",
           "Land claim and Aboriginal Land Rights (NT) Act 1976 research, including section 19 lease and consent processes",
           "Independent anthropological reports and peer reviews for lawyers, land councils and tribunals",
           "Traditional Owner identification and succession advice for agreements, royalties and distributions",
           "Historical, archival and museum collection research, including repatriation and provenance of cultural objects",
           "Culturally informed advice to boards, corporations and government on governance and decision-making"],
  who="Land councils and Native Title representative bodies, Aboriginal corporations and PBCs, law firms, NT and Commonwealth agencies, museums and research institutions.",
  pricing="Research is quoted per brief, usually as a capped number of days with milestones.",
  faqs=[("Can you act as an expert witness?","Helen Haritos prepares independent anthropological reports to the standard expected of an expert and can give evidence where required. Each brief is assessed for conflicts before acceptance."),
        ("Do you work outside the Northern Territory?","The practice is NT-focused with capacity for the East Kimberley region of Western Australia, where Helen has lived and worked. International archival research has been undertaken in Europe for Tiwi cultural objects."),
        ("How is confidential cultural information handled?","Restricted information stays with the people it belongs to. Reports distinguish between what can be published and what must remain confidential, and data is stored and shared under agreed protocols.")]),
 dict(slug="cultural-awareness-inductions", nav="Cultural awareness & inductions",
  title="Cultural Awareness Training & Heritage Inductions Darwin NT",
  h1="Cultural awareness training, heritage inductions and ceremony facilitation",
  desc="Project-specific cultural awareness sessions, sacred site and heritage inductions for construction crews, and facilitation of Welcome to Country and smoking ceremonies with Traditional Owners in Darwin and the Top End.",
  intro="Most heritage incidents on construction sites happen because somebody did not know. A half-day induction built around the actual project, its Authority Certificate and the people whose Country it is on prevents most of them, and sets the tone for the relationship with Traditional Owners.",
  bullets=["Project-specific cultural heritage and sacred site inductions for site crews, delivered on site or online",
           "Cultural awareness sessions for project teams, boards and government staff, grounded in the Country the project is on",
           "Facilitation of Welcome to Country, smoking ceremonies and site openings with the appropriate Traditional Owners, including payments and logistics",
           "Protocols for working with Traditional Owners, cultural monitors and communities",
           "Induction records and attendance registers for compliance files"],
  who="Head contractors mobilising a Darwin or Top End site, developers launching a project, government agencies and corporate teams working on Aboriginal land or with Aboriginal organisations.",
  pricing="Inductions and sessions are priced per session; ceremony facilitation is priced per event with Traditional Owner payments passed through at cost.",
  faqs=[("How do we arrange a Welcome to Country in Darwin?","A Welcome to Country should be given by a Larrakia Traditional Owner. Connected2Country identifies the right person for the location and occasion, agrees the fee, and handles the logistics so that the event is respectful and the relationship is sound."),
        ("Is a cultural induction the same as a general cultural awareness course?","No. A general course explains culture in the abstract. A project induction tells your crew which areas are restricted, what the Authority Certificate conditions mean on the ground, who the Traditional Owners are and what to do if something is found. Both have a place; the induction is the one that protects the project.")]),
 dict(slug="ai-digital-cultural-heritage", nav="AI & digital heritage services",
  title="AI & Digital Services for Cultural Heritage | Indigenous Data Sovereignty NT",
  h1="AI and digital services for cultural heritage",
  desc="Responsible use of AI and digital tools in cultural heritage: AI-assisted desktop assessments and research, secure cultural knowledge recording and archives, and Indigenous Data Sovereignty advice for Traditional Owner groups and proponents in the NT.",
  intro="AI is changing how heritage research, documentation and compliance are done. Connected2Country uses it to make desktop work faster and cheaper, while keeping the fieldwork, relationships and judgement with people, and helps Traditional Owner organisations set the rules for how their knowledge is recorded, stored and used.",
  bullets=["AI-assisted desktop assessments: rapid review of registers, reports, literature and archives, verified by the anthropologist before anything is relied on",
           "Digital recording and archiving of cultural knowledge, oral histories and collections, with access controls set by custodians",
           "Indigenous Data Sovereignty and AI governance advice for land councils, Aboriginal corporations and ranger groups, aligned with CARE principles and Maiam nayri Wingara guidance",
           "Advice to proponents and consultancies on what AI can and cannot do in heritage compliance, and what regulators and Traditional Owners will accept",
           "Digitisation and cataloguing support for community museums, keeping places and archives, building on work with the Patakijiyali Museum on the Tiwi Islands",
           "Plain-language cultural protocols for AI use within organisations working with Aboriginal knowledge"],
  who="Aboriginal corporations, land councils and ranger groups deciding how their knowledge is handled; museums and keeping places; environmental and heritage consultancies and proponents who want faster desktop work without compromising the fieldwork.",
  pricing="Advisory work is quoted per brief. AI-assisted desktop assessments are fixed price and typically cost less than conventional desktop studies.",
  faqs=[("Can AI replace an anthropologist for Traditional Owner consultation?","No. Consultation is a relationship between people about Country, and the legal and cultural weight of the outcome rests on that. AI is useful for the desktop work around it: finding and summarising what has already been recorded, drafting documents from field notes, and keeping registers current."),
        ("What is Indigenous Data Sovereignty?","The right of Indigenous peoples to govern the collection, ownership and application of data about their people, lands, knowledge and resources. For cultural heritage it means custodians decide what is recorded, who holds it, who can see it and whether it may be used to train or query AI systems."),
        ("Is cultural information safe in AI tools?","Only if the tool, the contract and the workflow are chosen for it. Public AI services may retain and reuse inputs. Connected2Country advises on tools and settings that do not train on your data, on what should never be entered at all, and on written protocols so staff know the difference.")]),
]

REGIONS = [
 dict(slug="darwin-palmerston-rural", nav="Darwin, Palmerston & Rural",
  title="Cultural Heritage Consultant Darwin, Palmerston & Rural Area NT",
  h1="Traditional Owner consultation and cultural heritage in Darwin, Palmerston and the rural area",
  desc="Darwin-based anthropologist for Traditional Owner consultation, AAPA Authority Certificate support and cultural heritage assessment across Darwin, Palmerston, Litchfield and the rural area on Larrakia and neighbouring country.",
  places="Darwin city and northern suburbs, Lee Point, Casuarina and the coastal reserves, East Arm, Berrimah and Winnellie, Darwin International Airport and RAAF Base precincts, Palmerston and its growth suburbs, Holtze, Howard Springs, Humpty Doo, Coolalinga, Berry Springs, Noonamah, Virginia, Bees Creek, the Litchfield municipality, Cox Peninsula, Dundee and the Finniss River country.",
  body="This is Connected2Country's home ground. Helen Haritos has lived in Darwin for decades and has worked with Larrakia and neighbouring Traditional Owners through the Northern Land Council, the NT Government and private practice. Being local means meetings can happen when Traditional Owners are available rather than when a fly-in consultant is, and that advice is grounded in how Darwin approvals, AAPA, the Heritage Branch and the Development Consent Authority actually work.",
  work=["Traditional Owner consultation for residential subdivisions and master-planned developments in the northern suburbs and Palmerston growth areas",
        "AAPA Authority Certificate support for infrastructure, utility and Defence precinct works",
        "Cultural heritage sections of CEMPs for civil contractors on NT Government and council contracts",
        "Welcome to Country and ceremony facilitation for project launches and openings",
        "Desktop and field heritage assessments for industrial land at East Arm, Berrimah and Winnellie and rural subdivisions in Litchfield"]),
 dict(slug="top-end", nav="Top End", img="region-top-end.jpg", img_alt="Landsat satellite image of Kakadu and the Arnhem Land escarpment, rendered in ochre tones", credit="Imagery: NASA/USGS Landsat (public domain)",
  title="Cultural Heritage & Traditional Owner Consultation Top End NT",
  h1="Traditional Owner consultation and cultural heritage across the Top End",
  desc="Anthropological services across the Top End: Katherine, Kakadu and West Arnhem, Arnhem Land, the Tiwi Islands, the Daly River and the Victoria River District. Land council experience, remote-capable, Wet-season aware.",
  places="Katherine and the Katherine River region, Pine Creek and Adelaide River, Kakadu and Jabiru, West Arnhem including Gunbalanya and Maningrida, East Arnhem including Nhulunbuy and Groote Eylandt, the Tiwi Islands (Wurrumiyanga, Pirlangimpi and Milikapiti), the Daly River and Wadeye, Batchelor and Litchfield, and the Victoria River District to Timber Creek.",
  body="Helen Haritos has over 20 years in Aboriginal land and heritage work in the Territory, including regional and senior anthropologist roles with the Northern Land Council and senior anthropologist with the Tiwi Land Council, working across the Top End on site surveys, land claims, mining and economic development consultations and Aboriginal Land Rights Act lease negotiations. That experience means Connected2Country knows the land council processes from the inside, understands how Traditional Owner decision-making works in remote communities and plans fieldwork around ceremony, sorry business and the Wet season.",
  work=["Sacred site surveys and Traditional Owner consultation for mining, energy, infrastructure and tourism proposals on Aboriginal land",
        "Section 19 lease and land use agreement consultations under the Aboriginal Land Rights (Northern Territory) Act 1976",
        "Cultural heritage and cultural values assessments for EIS projects",
        "Collection, archive and museum support for community keeping places, including the Tiwi Islands",
        "Cultural heritage management and inductions for remote construction programs"]),
 dict(slug="northern-territory-kimberley", nav="NT & East Kimberley", img="region-kimberley.jpg", img_alt="Landsat 9 satellite image of the Kimberley coast, Western Australia", credit="Imagery: NASA/USGS Landsat 9 (public domain)",
  title="Anthropologist for the Northern Territory & East Kimberley WA",
  h1="Anthropological services across the Northern Territory and into the East Kimberley",
  desc="Consultant anthropologist available Territory-wide, including Central Australia, and across the border into the East Kimberley of Western Australia: Kununurra, Wyndham, Lake Argyle and Halls Creek. Aboriginal Heritage Act 1972 (WA) and NT frameworks.",
  places="The whole of the Northern Territory including Tennant Creek, the Barkly, Alice Springs and Central Australia, and the East Kimberley region of Western Australia: Kununurra, Wyndham, Lake Argyle, the Ord River irrigation area, Halls Creek and the Great Northern Highway corridor.",
  body="For projects beyond the Top End, Connected2Country works with the relevant land council or Native Title representative body and local Traditional Owner organisations, and partners with regional specialists where that serves the client better. Helen has lived and worked in the East Kimberley and understands that heritage in Western Australia is governed by the Aboriginal Heritage Act 1972 as amended in 2023, with its section 18 consent process, the Aboriginal Cultural Heritage Inquiry System and the state's Aboriginal Heritage Survey Program, rather than the NT's AAPA and Heritage Act regime.",
  work=["Native title research and connection reports",
        "Anthropological input to heritage surveys and section 18 applications in the East Kimberley",
        "Traditional Owner consultation for cross-border infrastructure, agriculture and resources projects",
        "Independent anthropological reports and peer reviews",
        "AI and data governance advice to Aboriginal corporations and ranger groups"]),
]

GUIDES = [
 dict(slug="what-is-an-aapa-authority-certificate", title="What is an AAPA Authority Certificate and do I need one?",
  desc="How Authority Certificates under the NT Aboriginal Sacred Sites Act work, when a Darwin or Top End project should apply, what it costs in time, and how to avoid the common mistakes.",
  body="""<p>An Authority Certificate is a document issued by the Aboriginal Areas Protection Authority (AAPA) under the <em>Northern Territory Aboriginal Sacred Sites Act 1989</em>. It sets out the conditions under which proposed works can proceed without damaging or interfering with a sacred site, and it is a complete defence to prosecution under the Act if the works stay within those conditions.</p>
<h2>Why it matters</h2>
<p>Sacred sites are protected everywhere in the Northern Territory, on all tenures, whether or not they are registered and whether or not you know they are there. Damaging one is a criminal offence with penalties for both the company and individuals. The certificate is the only way to know in advance where the constraints are.</p>
<h2>When to apply</h2>
<ul><li>Any ground-disturbing works where sacred sites are plausible: coastal land, rivers and creeks, springs, rock outcrops, significant trees, and most undeveloped land around Darwin and Palmerston.</li><li>When a development permit, NT EPA approval, land council agreement or contract requires it.</li><li>When your financier, principal or insurer asks for it, which is increasingly common.</li></ul>
<h2>How the process works</h2>
<ol><li>Application to AAPA with a description of the works and a map of the area. Fees are set against project value.</li><li>AAPA checks its register and records and consults the custodians of any sites in or near the area, usually with field visits.</li><li>AAPA issues the certificate with conditions, often including restricted work areas (RWAs) with buffers and limits on particular activities.</li><li>The proponent builds the conditions into its management plans, inductions and site controls.</li></ol>
<h2>Common mistakes</h2>
<ul><li>Applying over too small an area, then needing a new certificate when the design changes.</li><li>Describing the works too narrowly, so that laydown areas, haul roads or borrow pits are not covered.</li><li>Treating the certificate as a tick-box and never translating the conditions for the site crew.</li><li>Leaving the application until after the program is set. Custodian consultation takes the time it takes.</li></ul>
<p>Connected2Country helps proponents scope the application, supports the custodian consultation and turns the conditions into something a site supervisor can work to. See <a href="/services/aapa-authority-certificate-sacred-sites/">AAPA Authority Certificate support</a>.</p>"""),
 dict(slug="traditional-owner-consultation-darwin-development", title="Do I need Traditional Owner consultation for my Darwin development?",
  desc="Which Darwin, Palmerston and rural area projects need Traditional Owner consultation, which approvals expect it, who the Larrakia Traditional Owners are, and how to do it properly.",
  body="""<p>For most development in the greater Darwin region the answer is yes, and the real question is how much and how early. The Larrakia people are the recognised Traditional Owners of the Darwin region, and several approval pathways either require their involvement or work far better with it.</p>
<h2>Approvals that expect consultation</h2>
<ul><li><strong>AAPA Authority Certificates</strong> are issued on the basis of consultation with custodians of sacred sites.</li><li><strong>NT EPA assessment</strong> of significant projects requires the proponent to assess impacts on culture and heritage, which cannot be done credibly without talking to Traditional Owners.</li><li><strong>Heritage Act 2011</strong> processes for Aboriginal archaeological places and declared heritage places involve the Heritage Council and, in practice, Traditional Owner views.</li><li><strong>Native Title</strong> future act procedures apply where native title has not been extinguished.</li><li><strong>Planning Act</strong> processes for rezoning and large subdivisions increasingly expect evidence of consultation, and Crown land and Darwin Waterfront, Defence and Commonwealth processes have their own requirements.</li></ul>
<h2>Who to consult</h2>
<p>Identifying the right people is anthropological work, not a mailing list. Larrakia country has family groups with particular connections to particular places, and some areas on the edges of the region are shared with or claimed by neighbouring groups. Getting this wrong is the most common reason consultation is later challenged.</p>
<h2>What good consultation looks like</h2>
<ul><li>Started early, before the design is fixed.</li><li>Plain information about what is proposed, with maps and site visits.</li><li>Time for people to talk among themselves and come back.</li><li>Records that show who was consulted, what they said and what changed as a result.</li><li>Fair payment for people's time and expertise.</li></ul>
<p>Connected2Country runs this process for developers and contractors across Darwin, Palmerston and the rural area. See <a href="/services/traditional-owner-consultation/">Traditional Owner consultation</a>.</p>"""),
 dict(slug="nt-heritage-laws-explained", title="NT heritage laws explained: Sacred Sites Act, Heritage Act and the Land Rights Act",
  desc="A plain-English guide to the three laws that govern Aboriginal cultural heritage in the Northern Territory, who administers each, and how they interact on a typical project.",
  body="""<p>Three pieces of legislation do most of the work in protecting Aboriginal cultural heritage in the Northern Territory. Projects often need to deal with more than one.</p>
<h2>Northern Territory Aboriginal Sacred Sites Act 1989</h2>
<p>Protects sacred sites, which are places of significance under Aboriginal tradition, on all land in the Territory. Administered by the Aboriginal Areas Protection Authority (AAPA), which keeps a register, consults custodians and issues Authority Certificates. Offences apply whether or not a site is registered.</p>
<h2>Heritage Act 2011 (NT)</h2>
<p>Protects declared heritage places and objects, and gives automatic protection to all Aboriginal and Macassan archaeological places and objects. Administered by the Heritage Branch with advice from the NT Heritage Council. Works that may affect a protected place need approval, and unexpected finds must be reported.</p>
<h2>Aboriginal Land Rights (Northern Territory) Act 1976 (Cth)</h2>
<p>Grants inalienable freehold title to Aboriginal land trusts over roughly half of the Territory and requires that Traditional Owners consent, through the relevant land council, to leases, mining and other uses of that land. Section 19 leases and section 42 to 48 mining provisions are the parts proponents meet most often. Land councils employ anthropologists to identify Traditional Owners and run consultations.</p>
<h2>And the rest</h2>
<p>The <em>Native Title Act 1993</em> (Cth) applies where native title survives on non-Aboriginal land; the <em>Environment Protection Act 2019</em> (NT) requires culture and heritage to be assessed for significant projects; and the Commonwealth <em>Aboriginal and Torres Strait Islander Heritage Protection Act 1984</em> is a last-resort protection.</p>
<h2>How they fit together on a project</h2>
<p>A subdivision on freehold land near the Darwin coast might need an AAPA Authority Certificate, a Heritage Act check for archaeological places, and Traditional Owner consultation for the NT EPA or planning process. A road on Aboriginal land near Maningrida needs land council consent under the Land Rights Act plus the certificate. Working out the pathway early is most of the value an anthropologist adds. See <a href="/services/cultural-heritage-assessment/">cultural heritage assessment</a>.</p>"""),
 dict(slug="ai-in-cultural-heritage-what-changes", title="AI in cultural heritage work: what changes and what does not",
  desc="How AI is changing heritage research, documentation and compliance, where it helps, where it is risky, and the questions Traditional Owner organisations and proponents should be asking.",
  body="""<p>AI tools can now read a decade of heritage reports in an afternoon, draft a management plan from field notes, transcribe interviews and keep registers current. That changes the economics of desktop work. It does not change what gives heritage work its legal and cultural weight.</p>
<h2>What AI does well</h2>
<ul><li>Finding and summarising what has already been recorded about a place across registers, reports, archives and literature.</li><li>Drafting documents from the anthropologist's field notes, so that the human time goes into the fieldwork and the judgement.</li><li>Transcribing and indexing oral histories, with custodian control over access.</li><li>Keeping consultation registers, condition registers and compliance records current.</li></ul>
<h2>What stays with people</h2>
<ul><li>Identifying who speaks for Country. This is relationship and knowledge, and the answer is contested often enough that it must be defensible.</li><li>Consultation itself. Consent given to a person on Country is what regulators, courts and communities recognise.</li><li>Assessing significance and giving expert opinion.</li><li>Deciding what knowledge is recorded at all, and what must stay restricted.</li></ul>
<h2>The risks</h2>
<ul><li>Confidential cultural information entered into public AI services that retain and reuse inputs.</li><li>Fluent, confident summaries of sources that do not say what the summary claims. Every AI output in heritage work needs verification against the source.</li><li>Reports that look complete but were never checked by someone who has been on the Country.</li><li>Organisations adopting tools with no protocol, so staff make the decisions by accident.</li></ul>
<h2>Questions to ask</h2>
<p>Who owns the data? Where is it stored and is it used for training? Who verified the output? What is the protocol for restricted knowledge? Would the Traditional Owners whose knowledge this is agree with how it is being handled?</p>
<p>Connected2Country uses AI for the desktop work, verifies everything, and helps organisations write the rules. See <a href="/services/ai-digital-cultural-heritage/">AI and digital services for cultural heritage</a>.</p>"""),
]

# ------------------------------------------------------------------ helpers
def esc(s): return html.escape(s, quote=True)
def ld(obj): return '<script type="application/ld+json">'+json.dumps(obj, ensure_ascii=False)+'</script>'

AREAS=[{"@type":"City","name":"Darwin"},{"@type":"City","name":"Palmerston"},{"@type":"AdministrativeArea","name":"Litchfield Municipality"},
       {"@type":"Place","name":"Top End, Northern Territory"},{"@type":"State","name":"Northern Territory"},{"@type":"Place","name":"East Kimberley, Western Australia"}]
ORG = {"@type":"ProfessionalService","@id":BASE+"/#org","name":BRAND,"alternateName":["Connected 2 Country Anthropology","C2C"],"url":BASE+"/",
  "logo":BASE+"/assets/logo.png","image":BASE+"/assets/og.png","telephone":PHONE_INTL,"email":EMAIL,
  "description":"Consultant anthropologist and archaeologist based in Darwin providing Traditional Owner consultation, AAPA Authority Certificate support, cultural heritage assessment, heritage management plans, native title research, cultural inductions and AI and data governance advice across the Northern Territory and East Kimberley.",
  "address":{"@type":"PostalAddress","addressLocality":"Fannie Bay","addressRegion":"NT","postalCode":"0820","addressCountry":"AU"},
  "geo":{"@type":"GeoCoordinates","latitude":-12.43,"longitude":130.84},
  "areaServed":AREAS,"vatID":"ABN "+ABN,
  "founder":{"@type":"Person","@id":BASE+"/about/#helen","name":"Helen Haritos","jobTitle":"Consultant Anthropologist and Archaeologist"},
  "priceRange":"$$","knowsAbout":["Traditional Owner consultation","Aboriginal sacred sites Northern Territory","AAPA Authority Certificates","Cultural heritage assessment","Native title research","Aboriginal Land Rights (Northern Territory) Act","Larrakia","Tiwi Islands","Indigenous Data Sovereignty"],
  "sameAs":[]}

def layout(path, title, desc, body, extra_ld=None):
    canonical = BASE + path
    lds = [dict(ORG, **{"@context":"https://schema.org"})] if path=="/" else []
    if extra_ld: lds += extra_ld
    svc_links = "".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["nav"])}</a></li>' for s in SERVICES)
    reg_links = "".join(f'<li><a href="/regions/{r["slug"]}/">{esc(r["nav"])}</a></li>' for r in REGIONS)
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="AU-NT"><meta name="geo.placename" content="Darwin">
<link rel="icon" href="/assets/favicon.png" type="image/png">
<link rel="stylesheet" href="/assets/style.css">{'<link rel="preload" as="image" href="/assets/hero.jpg">' if path=='/' else ''}
{''.join(ld(x) for x in lds)}
</head>
<body>
<header class="top">
 <div class="wrap bar">
  <a class="logo" href="/"><img src="/assets/logo.png" alt="Connected2Country — Connected to Country" width="80" height="56"></a>
  <nav aria-label="Main">
   <input type="checkbox" id="m" hidden><label for="m" class="burger" aria-label="Menu">☰</label>
   <ul>
    <li class="dd"><a href="/services/">Services</a><ul>{svc_links}</ul></li>
    <li class="dd"><a href="/regions/">Regions</a><ul>{reg_links}</ul></li>
    <li><a href="/guides/">Guides</a></li>
    <li><a href="/about/">About</a></li>
    <li><a class="btn" href="/contact/">Contact</a></li>
   </ul>
  </nav>
 </div>
</header>
<main>
{body}
</main>
<footer>
 <div class="wrap grid3">
  <div><h3>{BRAND}</h3><p>Consultant anthropologist and archaeologist. Traditional Owner consultation, sacred sites and cultural heritage for the Northern Territory. Darwin-based, Territory-wide, East Kimberley-capable.</p>
   <p><a href="tel:{PHONE_INTL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Fannie Bay NT 0820</p></div>
  <div><h3>Services</h3><ul>{svc_links}</ul></div>
  <div><h3>Regions</h3><ul>{reg_links}</ul><h3>More</h3><ul><li><a href="/guides/">Guides</a></li><li><a href="/about/">About Helen Haritos</a></li><li><a href="/contact/">Contact</a></li></ul></div>
 </div>
 <div class="wrap fine"><p>Connected2Country acknowledges the Larrakia people, Traditional Owners of the Darwin region, and all Traditional Owners of the Country on which we work, and pays respect to Elders past and present.</p>
 <p>Helen Maria Haritos trading as Connected2Country, ABN {ABN}. © {BRAND} {TODAY[:4]}. Satellite imagery courtesy NASA/USGS Landsat and the International Space Station (public domain).</p></div>
</footer>
</body>
</html>"""

def banner(d):
    if not d.get("img"): return ""
    return f'<figure class="banner"><img src="/assets/{d["img"]}" alt="{esc(d["img_alt"])}" width="1400" height="560" loading="lazy"><figcaption>{esc(d["credit"])}</figcaption></figure>'

def cta(text="Talk to Helen about your project"):
    return f'<div class="cta"><p>{esc(text)}</p><a class="btn big" href="/contact/">Get a scoped quote</a> <a class="btn ghost" href="tel:{PHONE_INTL}">Call {PHONE}</a></div>'
def faq_html(faqs):
    return '<section class="wrap"><h2>Frequently asked questions</h2>'+"".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in faqs)+'</section>'
def faq_ld(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
def crumbs(items):
    lst=[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]
    h='<nav class="crumbs wrap" aria-label="Breadcrumb">'+" › ".join(f'<a href="{u}">{esc(n)}</a>' for n,u in items)+'</nav>'
    return h,{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":lst}
def write(path, content):
    p = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"): p = os.path.join(p, "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p,"w",encoding="utf-8").write(content)

pages = []

# ------------------------------------------------------------------ pages
def home():
    cards = "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{esc(s["h1"])}</h3><p>{esc(s["desc"].split(". ")[0])}.</p></a>' for s in SERVICES)
    regs = "".join(f'<a class="card" href="/regions/{r["slug"]}/"><h3>{esc(r["nav"])}</h3><p>{esc(r["places"].split(",")[0])} and surrounds</p></a>' for r in REGIONS)
    guides = "".join(f'<li><a href="/guides/{g["slug"]}/">{esc(g["title"])}</a></li>' for g in GUIDES)
    body = f"""
<section class="hero hero-img"><div class="wrap">
 <p class="kicker">Consultant anthropologist · Darwin NT</p>
 <h1>Traditional Owner consultation and cultural heritage advice that gets Territory projects approved, and keeps them that way.</h1>
 <p class="lead">Connected2Country is the practice of Helen Haritos, an anthropologist and archaeologist with over 20 years in Aboriginal land, heritage and native title work in the NT. Traditional Owner consultation, AAPA Authority Certificate support, cultural heritage assessment, management plans, native title research and responsible use of AI in heritage work.</p>
 <p><a class="btn big" href="/contact/">Get a scoped quote</a> <a class="btn ghost" href="tel:{PHONE_INTL}">Call {PHONE}</a></p>
 <p class="small">Servicing <a href="/regions/darwin-palmerston-rural/">Darwin, Palmerston and the rural area</a>, the <a href="/regions/top-end/">Top End</a>, and the <a href="/regions/northern-territory-kimberley/">wider NT and East Kimberley</a>.</p>
</div></section>
<section class="wrap"><h2>Services</h2><div class="cards">{cards}</div></section>
<section class="alt"><div class="wrap"><h2>Why proponents and consultancies use Connected2Country</h2><div class="cols">
 <div><h3>Over 20 years on Country</h3><p>More than two decades in NT Aboriginal land and heritage work, including senior anthropologist roles with the Northern Land Council and Tiwi Land Council. Helen knows how Traditional Owner decisions are made and how land councils, AAPA and the Heritage Branch assess what you submit.</p></div>
 <div><h3>Anthropology and archaeology</h3><p>Both disciplines in one practitioner: the intangible values and the right people to speak, plus the archaeological places the Heritage Act protects.</p></div>
 <div><h3>Local and available</h3><p>Darwin-based, so consultation happens when Traditional Owners are available, not when flights are. Remote-capable across the Top End and into the East Kimberley.</p></div>
 <div><h3>Modern tools, human judgement</h3><p>AI handles the desktop reading, drafting and registers so that expert time goes into Country, people and the judgement calls. Faster and cheaper desktop work without cutting corners on the fieldwork.</p></div>
</div></div></section>
<section class="wrap"><h2>Where we work</h2><div class="cards">{regs}</div></section>
<section class="alt"><div class="wrap"><h2>Who we work with</h2><p class="chips"><span>Developers</span><span>Civil contractors</span><span>Heritage &amp; environmental consultancies</span><span>NT Government</span><span>Defence</span><span>Land councils</span><span>Aboriginal corporations</span><span>Law firms</span><span>Museums &amp; keeping places</span><span>Resources &amp; energy</span></p>
<p class="small">Connected2Country works alongside <a href="https://bellenviro.au/" rel="noopener">Bell Enviro</a> to deliver integrated environment and heritage approvals and management plans for civil projects.</p></div></section>
<section class="wrap"><h2>Guides</h2><ul class="list">{guides}</ul></section>
{cta("Tell Helen where the project is and what approval you are chasing, and get a scoped price back, usually within two business days.")}
"""
    write("/", layout("/", "Anthropologist Darwin NT | Traditional Owner Consultation, Sacred Sites & Cultural Heritage | Connected2Country",
        "Darwin-based consultant anthropologist for Traditional Owner consultation, AAPA Authority Certificate support, cultural heritage assessment, heritage management plans and native title research across the NT and East Kimberley.", body))
    pages.append(("/",1.0))

def services_index():
    cards = "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{esc(s["h1"])}</h3><p>{esc(s["desc"])}</p></a>' for s in SERVICES)
    ch,cl = crumbs([("Home","/"),("Services","/services/")])
    body = f'{ch}<section class="wrap"><h1>Anthropology and cultural heritage services</h1><p class="lead">Every engagement is scoped and priced before work starts and delivered by Helen Haritos. Pick the service that matches the approval condition, the contract clause or the question you are facing.</p><div class="cards">{cards}</div></section>{cta()}'
    write("/services/", layout("/services/","Cultural Heritage & Anthropology Services NT | Connected2Country","Traditional Owner consultation, AAPA certificates and sacred sites, cultural heritage assessment, management plans, native title research, inductions and AI and digital heritage services for the Northern Territory.", body,[cl]))
    pages.append(("/services/",0.8))

def service(s):
    path=f"/services/{s['slug']}/"
    ch,cl = crumbs([("Home","/"),("Services","/services/"),(s["nav"],path)])
    svc_ld={"@context":"https://schema.org","@type":"Service","name":s["h1"],"serviceType":s["nav"],"description":s["desc"],"provider":{"@id":BASE+"/#org"},"areaServed":AREAS,"url":BASE+path}
    regs=" · ".join(f'<a href="/regions/{r["slug"]}/">{esc(r["nav"])}</a>' for r in REGIONS)
    body=f"""{ch}
<section class="wrap"><h1>{esc(s['h1'])}</h1><p class="lead">{esc(s['intro'])}</p>{banner(s)}
<h2>What is included</h2><ul class="ticks">{''.join(f'<li>{esc(b)}</li>' for b in s['bullets'])}</ul>
<h2>Who it is for</h2><p>{esc(s['who'])}</p>
<h2>Pricing</h2><p>{esc(s['pricing'])}</p>
<p class="small">Available in {regs}.</p></section>
{faq_html(s['faqs'])}
{cta()}"""
    write(path, layout(path, s["title"], s["desc"], body,[cl,svc_ld,faq_ld(s["faqs"])]))
    pages.append((path,0.9))

def regions_index():
    cards="".join(f'<a class="card" href="/regions/{r["slug"]}/"><h3>{esc(r["h1"])}</h3><p>{esc(r["desc"])}</p></a>' for r in REGIONS)
    ch,cl=crumbs([("Home","/"),("Regions","/regions/")])
    body=f'{ch}<section class="wrap"><h1>Where Connected2Country works</h1><p class="lead">Based in Darwin, working across the Top End, the Northern Territory and into the East Kimberley.</p><div class="cards">{cards}</div></section>{cta()}'
    write("/regions/", layout("/regions/","Service Regions | Darwin, Top End, NT & East Kimberley | Connected2Country","Anthropological and cultural heritage services for Darwin, Palmerston and the rural area, the Top End, the wider Northern Territory and the East Kimberley.", body,[cl]))
    pages.append(("/regions/",0.7))

def region(r):
    path=f"/regions/{r['slug']}/"
    ch,cl=crumbs([("Home","/"),("Regions","/regions/"),(r["nav"],path)])
    svcs="".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["h1"])}</a></li>' for s in SERVICES)
    body=f"""{ch}
<section class="wrap"><h1>{esc(r['h1'])}</h1>{banner(r)}<p class="lead">{esc(r['body'])}</p>
<h2>Areas covered</h2><p>{esc(r['places'])}</p>
<h2>Typical work in this region</h2><ul class="ticks">{''.join(f'<li>{esc(w)}</li>' for w in r['work'])}</ul>
<h2>Services available</h2><ul class="list">{svcs}</ul></section>
{cta()}"""
    write(path, layout(path, r["title"], r["desc"], body,[cl]))
    pages.append((path,0.8))

def guides_index():
    items="".join(f'<a class="card" href="/guides/{g["slug"]}/"><h3>{esc(g["title"])}</h3><p>{esc(g["desc"])}</p></a>' for g in GUIDES)
    ch,cl=crumbs([("Home","/"),("Guides","/guides/")])
    body=f'{ch}<section class="wrap"><h1>Guides to cultural heritage in the Northern Territory</h1><p class="lead">Plain answers to the questions proponents, contractors and organisations ask before a project starts.</p><div class="cards">{items}</div></section>{cta()}'
    write("/guides/", layout("/guides/","Cultural Heritage Guides for NT Projects | Connected2Country","Plain-English guides on AAPA Authority Certificates, Traditional Owner consultation, NT heritage laws and AI in cultural heritage work.", body,[cl]))
    pages.append(("/guides/",0.6))

def guide(g):
    path=f"/guides/{g['slug']}/"
    ch,cl=crumbs([("Home","/"),("Guides","/guides/"),(g["title"],path)])
    art={"@context":"https://schema.org","@type":"Article","headline":g["title"],"description":g["desc"],"datePublished":TODAY,"dateModified":TODAY,
         "author":{"@id":BASE+"/about/#helen"},"publisher":{"@id":BASE+"/#org"},"mainEntityOfPage":BASE+path}
    body=f'{ch}<article class="wrap prose"><h1>{esc(g["title"])}</h1><p class="small">By Helen Haritos, Consultant Anthropologist, Connected2Country · Updated {TODAY}</p>{g["body"]}<p class="small">General information only, not legal advice. Legislation and agency practice change; check current requirements with AAPA, the Heritage Branch or the relevant land council.</p></article>{cta()}'
    write(path, layout(path, g["title"]+" | Connected2Country", g["desc"], body,[cl,art]))
    pages.append((path,0.7))

def about():
    ch,cl=crumbs([("Home","/"),("About","/about/")])
    person={"@context":"https://schema.org","@type":"Person","@id":BASE+"/about/#helen","name":"Helen Haritos","jobTitle":"Consultant Anthropologist and Archaeologist","worksFor":{"@id":BASE+"/#org"},
            "email":EMAIL,"telephone":PHONE_INTL,"url":BASE+"/about/","image":BASE+"/assets/helen.jpg","knowsAbout":ORG["knowsAbout"],
            "alumniOf":{"@type":"CollegeOrUniversity","name":"Charles Darwin University"},
            "hasCredential":[{"@type":"EducationalOccupationalCredential","name":"BA (Hons) Archaeology, Charles Darwin University"},{"@type":"EducationalOccupationalCredential","name":"Graduate Diploma of Languages (Hellenic Studies), Charles Darwin University"}],
            "memberOf":[{"@type":"Organization","name":"Australian Anthropological Society"},{"@type":"Organization","name":"American Anthropological Association"},{"@type":"Organization","name":"Archaeological and Anthropological Society of Victoria"},{"@type":"Organization","name":"World Archaeological Congress"}]}
    body=f"""{ch}
<section class="wrap prose"><img class="portrait" src="/assets/helen.jpg" alt="Helen Haritos, Consultant Anthropologist, Connected2Country, in the field in the Northern Territory" width="600" height="600" loading="eager"><h1>About Connected2Country and Helen Haritos</h1>
<p class="lead">Connected2Country is the consulting practice of Helen Haritos, an anthropologist and archaeologist who has lived in Darwin for most of her life and has over 20 years in Aboriginal land, heritage and native title work in the Northern Territory, including senior anthropologist roles in land councils, before moving into private practice.</p>
<h2>Experience</h2>
<ul>
<li><strong>Senior Anthropologist, Tiwi Land Council (2022–2024):</strong> engagement with Tiwi Islanders, section 19 Land Rights Act lease negotiations, formation of the Tiwi cultural committee, sacred site surveys with AAPA, curation of artefact collections, and a flora and fauna clearance survey at the Osprey crash site.</li>
<li><strong>Senior Anthropologist, Northern Land Council (2017–2021):</strong> research and review of land claim findings, consultations with Traditional Owners, anthropological reports, genealogies and sacred site records.</li>
<li><strong>Regional Anthropologist, Northern Land Council (2008–2017):</strong> site surveys and clearances, Traditional Owner consultations, genealogies, economic development and mining project consultations, and native title case support across the Top End.</li>
<li><strong>Researcher, Archaeology of the Tiwi Islands Project (2024):</strong> international archival research in Leiden, Rome and Paris on Tiwi cultural objects.</li>
<li><strong>Archivist and research support, Patakijiyali Museum, Wurrumiyanga (2024–2025):</strong> cataloguing and preparing photographs, film and literature for digitisation with Tiwi women.</li>
<li><strong>NT Government, Department of Primary Industry, Fisheries and Mines (2003–2008):</strong> ALRA Unit project officer advising on exploration and mining on Aboriginal land and compliance under the Land Rights and Native Title Acts, then Senior Titles Officer, Petroleum.</li>
<li><strong>Archaeologist, EcOz Environmental Services (2003):</strong> archaeological surveys for the Trans Territory Pipeline corridor.</li>
<li><strong>Anthropologist and archaeologist with Bell Enviro (2023–present):</strong> cultural heritage consultation, compliance inspections and audits, AAPA clearance consultations and ethno-ecology advice for civil and development projects.</li>
</ul>
<h2>Qualifications and memberships</h2>
<ul><li>BA (Hons) Archaeology, Charles Darwin University</li><li>Graduate Diploma of Languages (Hellenic Studies) and Certificate of Arts (Hellenic Studies), Charles Darwin University</li><li>Native Title Guided Research Placement, ANU Centre for Native Title Anthropology, with Dr Julie Finlayson and Professor Nicholas Peterson</li><li>Introduction to Maritime Archaeology (AIMA/NAS)</li><li>Member, Australian Anthropological Society; American Anthropological Association; Archaeological and Anthropological Society of Victoria; World Archaeological Congress (Independent Scholar)</li></ul>
<h2>Community</h2>
<p>Chairperson of Friends of East Point Inc (2007–2019), Deputy President of University Women of Australia NT Branch (2004–2008), and long involvement with the Historical Society of the Northern Territory. Helen has also lived and worked in the East Kimberley.</p>
<h2>How the practice works</h2>
<p>Every engagement is delivered by Helen. For larger programs she draws on trusted archaeologists, interpreters, cultural advisers and GIS support, and works alongside <a href="https://bellenviro.au/" rel="noopener">Bell Enviro</a> where a project needs environment and heritage handled together. Modern tools, including AI, are used for desktop research, drafting and record-keeping; fieldwork, relationships and professional judgement are not delegated.</p>
<p>Connected2Country acknowledges the Larrakia people as Traditional Owners of the Darwin region, and the Traditional Owners of all the Country on which it works.</p>
</section>{cta("Want to know whether Connected2Country is the right fit for your project? A ten-minute call usually settles it.")}"""
    write("/about/", layout("/about/","About Helen Haritos | Consultant Anthropologist & Archaeologist, Darwin NT","Helen Haritos is a Darwin-based anthropologist and archaeologist with over 20 years in NT Aboriginal land and heritage work, now providing Traditional Owner consultation and cultural heritage services through Connected2Country.", body,[cl,person]))
    pages.append(("/about/",0.6))

def contact():
    ch,cl=crumbs([("Home","/"),("Contact","/contact/")])
    body=f"""{ch}
<section class="wrap two"><div>
<h1>Contact Connected2Country</h1>
<p class="lead">Send the project location, the approval or condition you are working to, and any dates, and Helen will come back with a scoped price, usually within two business days.</p>
<p><strong>Helen Haritos</strong>, Consultant Anthropologist<br><a href="tel:{PHONE_INTL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Fannie Bay NT 0820<br>Servicing Darwin, Palmerston, the Top End, the NT and the East Kimberley</p>
<p class="small">ABN {ABN}. Hours: Monday to Friday, 8:00am to 5:00pm ACST. Unexpected finds and incident support by phone.</p>
</div>
<form class="form" action="/contact.php" method="post">
 <label>Name<input name="name" required maxlength="100"></label>
 <label>Organisation<input name="company" maxlength="100"></label>
 <label>Email<input name="email" type="email" required maxlength="150"></label>
 <label>Phone<input name="phone" type="tel" maxlength="40"></label>
 <label>Service needed<select name="service">{''.join(f'<option>{esc(s["nav"])}</option>' for s in SERVICES)}<option>Not sure yet</option></select></label>
 <label>Project location<input name="location" maxlength="150" placeholder="e.g. Lee Point, Palmerston, Jabiru, Kununurra"></label>
 <label>Tell Helen about the project<textarea name="message" rows="6" required maxlength="4000"></textarea></label>
 <div class="hp"><label>Leave blank<input name="website" tabindex="-1" autocomplete="off"></label></div>
 <input type="hidden" name="ts" value="">
 <button class="btn big" type="submit">Send enquiry</button>
 <p class="small">Attachments (approval conditions, Authority Certificates, drawings, previous reports) can be emailed to {EMAIL} after sending.</p>
</form></section>
<script>document.querySelector('[name=ts]').value=Date.now();</script>"""
    write("/contact/", layout("/contact/","Contact Connected2Country | Anthropologist Darwin NT","Request a scoped quote for Traditional Owner consultation, AAPA certificate support, cultural heritage assessment or anthropological research in Darwin and the NT. Call 0438 805 294.", body,[cl]))
    pages.append(("/contact/",0.8))
    write("/thanks/", layout("/thanks/","Thanks | Connected2Country","Your enquiry has been sent to Connected2Country.", '<section class="wrap"><h1>Thanks, your enquiry is on its way.</h1><p class="lead">Helen will reply within two business days. If it is urgent, call <a href="tel:'+PHONE_INTL+'">'+PHONE+'</a>.</p><p><a class="btn" href="/">Back to home</a></p></section>'))
    write("/404.html", layout("/404.html","Page not found | Connected2Country","That page does not exist.", '<section class="wrap"><h1>Page not found</h1><p class="lead">Try the <a href="/services/">services</a>, <a href="/regions/">regions</a> or <a href="/guides/">guides</a> pages, or go <a href="/">home</a>.</p></section>'))

def statics():
    os.makedirs(os.path.join(OUT,"assets"),exist_ok=True)
    for f in ("style.css","logo.png","favicon.png","og.png","helen.jpg","hero.jpg","region-top-end.jpg","region-kimberley.jpg","heritage-plateau.jpg"): shutil.copy("assets/"+f, os.path.join(OUT,"assets",f))
    shutil.copy("contact.php", os.path.join(OUT,"contact.php")); shutil.copy("htaccess", os.path.join(OUT,".htaccess"))
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(
        f'<url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n' for p,pr in pages)+'</urlset>\n'
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    bots=["GPTBot","OAI-SearchBot","ChatGPT-User","ClaudeBot","Claude-SearchBot","Claude-User","anthropic-ai","PerplexityBot","Perplexity-User","Google-Extended","Applebot-Extended","Bingbot","Amazonbot","meta-externalagent"]
    robots="User-agent: *\nAllow: /\nDisallow: /contact.php\nDisallow: /thanks/\n\n# AI crawlers explicitly welcome\n"+"".join(f"User-agent: {b}\nAllow: /\n" for b in bots)+f"\nSitemap: {BASE}/sitemap.xml\n"
    open(os.path.join(OUT,"robots.txt"),"w").write(robots)
    llms=f"# {BRAND}\n\n> Consultant anthropologist and archaeologist (Helen Haritos) based in Darwin, Northern Territory, Australia. Provides Traditional Owner and Native Title holder consultation, AAPA Authority Certificate support and sacred site advice, cultural heritage and cultural values assessments, Cultural Heritage Management Plans and CEMP heritage sections, native title and anthropological research and expert reports, cultural awareness inductions and ceremony facilitation, and AI/digital services for cultural heritage including Indigenous Data Sovereignty advice. Over 20 years in NT Aboriginal land, heritage and native title work, including senior anthropologist roles with the Northern Land Council and Tiwi Land Council. Phone {PHONE}. Email {EMAIL}. ABN {ABN}.\n\n"
    llms+="Service regions in priority order: (1) Darwin, Palmerston and the Litchfield rural area (Larrakia country); (2) the Top End including Katherine, Kakadu, Arnhem Land, the Tiwi Islands and the Daly; (3) the wider Northern Territory and the East Kimberley region of Western Australia (Kununurra, Wyndham, Halls Creek).\n\n## Services\n"
    llms+="".join(f"- [{s['h1']}]({BASE}/services/{s['slug']}/): {s['desc']}\n" for s in SERVICES)
    llms+="\n## Regions\n"+"".join(f"- [{r['h1']}]({BASE}/regions/{r['slug']}/): {r['desc']}\n" for r in REGIONS)
    llms+="\n## Guides\n"+"".join(f"- [{g['title']}]({BASE}/guides/{g['slug']}/): {g['desc']}\n" for g in GUIDES)
    llms+=f"\n## Other\n- [About Helen Haritos]({BASE}/about/)\n- [Contact]({BASE}/contact/)\n\n## Partner\n- [Bell Enviro](https://bellenviro.au/): environmental consultancy; integrated environment and heritage approvals.\n"
    open(os.path.join(OUT,"llms.txt"),"w").write(llms)
    # llms-full.txt: plain-text dump of every page for AI agents
    import re
    full=[llms]
    for s in SERVICES:
        full.append(f"\n\n# {s['h1']}\nURL: {BASE}/services/{s['slug']}/\n\n{s['intro']}\n\nIncluded:\n"+"".join(f"- {b}\n" for b in s['bullets'])+f"\nWho it is for: {s['who']}\nPricing: {s['pricing']}\n\nFAQ:\n"+"".join(f"Q: {q}\nA: {a}\n" for q,a in s['faqs']))
    for r in REGIONS:
        full.append(f"\n\n# {r['h1']}\nURL: {BASE}/regions/{r['slug']}/\n\n{r['body']}\n\nAreas: {r['places']}\n\nTypical work:\n"+"".join(f"- {w}\n" for w in r['work']))
    for g in GUIDES:
        txt=re.sub(r'<[^>]+>',' ',g['body']); txt=re.sub(r'\s+',' ',html.unescape(txt)).strip()
        full.append(f"\n\n# {g['title']}\nURL: {BASE}/guides/{g['slug']}/\n\n{txt}")
    open(os.path.join(OUT,"llms-full.txt"),"w").write("".join(full))

if __name__=="__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    home(); services_index(); [service(s) for s in SERVICES]
    regions_index(); [region(r) for r in REGIONS]
    guides_index(); [guide(g) for g in GUIDES]
    about(); contact(); statics()
    print(f"built {len(pages)} pages -> {OUT}/")
