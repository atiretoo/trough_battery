historical trough batttery
https://gemini.google.com/app/cd502d816727a98f
User prompt: I’m thinking about making a replica of a trough battery. I’m wondering if there are any
materials other than copper that would work as a primary cell with zinc anode.
Response: Several cathode materials can replace copper when paired with a zinc anode, ranging
from direct historical substitutes to modern conductive materials.
Conductive & Catalytic Cathode Materials
Graphite / Porous Carbon: The most practical and chemically stable alternative. Carbon
acts as an inert electronic conductor for hydrogen evolution (or oxygen reduction if exposed to
air). It yields an open-circuit potential around 1.2 V to 1.4 V against zinc in dilute acid or
neutral chloride/sulfate electrolytes.
Platinized Silver (The Smee Cell): Historically developed by Alfred Smee in 1840 to replace
copper in early trough and immersion batteries. The finely divided platinum black deposited
onto silver drastically lowers the overpotential for hydrogen gas evolution, preventing
hydrogen bubbles from clinging to the plate and resisting the rapid polarization typical of plain
copper.
Silver Sheet: Higher standard electrode potential than copper (  vs.
 for copper), resulting in a cell voltage around 1.55 V against zinc, though expensive
for large plates.
Nickel or Stainless Steel (316L): Functions similarly to copper in neutral salt or alkaline
electrolytes with reasonable chemical resistance. However, in dilute sulfuric or hydrochloric
acid, stainless steel may passivate or pit depending on the acid concentration, yielding a
lower cell voltage (~0.7 V to 0.9 V).
Depolarized Metal Oxide Cathodes
In a simple trough with single-fluid electrolytes (like dilute sulfuric acid or brine), plain metal
cathodes polarize rapidly due to insulating hydrogen gas formation ( ).
Incorporating an active depolarizer or metal oxide maintains a higher, steady current:
Manganese Dioxide ( ) on Carbon: Forming a composite plate or packing 
/carbon paste into porous cathode frames recreates the Leclanché primary chemistry,
producing a steady 1.5 V in ammonium chloride, zinc chloride, or sodium chloride electrolyte
without significant gas evolution.
Lead Dioxide ( ): Used in early acid-based bichromate or acid-zinc cells. A  plate
paired with zinc in dilute sulfuric acid delivers an open-circuit potential over 2.4 V, though it
requires careful handling of lead and strong acid.
E =∘ +0.80 V
+0.34 V
2H ++ 2e →− H  
2
MnO
 
2 MnO
 
2
PbO  
2 PbO  
2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 1/92
Cathode
Material Electrolyte Approximate
OCV
Primary Advantage /
Behavior
Graphite /
Carbon
Dilute  or 
/ 1.2 – 1.4 V Zero corrosion; easy to source
or fabricate into flat sheets.
Platinized Silver
/ Titanium Dilute ~1.0 V Fast hydrogen release;
historical Smee battery design.
Silver Dilute  or ~1.5 V Higher voltage than copper;
very low internal resistance.
Matrix
 or ~1.5 V Eliminates  polarization;
high current capacity.
316 Stainless
Steel
 or 
(neutral) 0.7 – 0.9 V Readily available rigid sheet
stock for structural mockups.
User prompt: Would grafoil work? Not historically accurate but I have it
Response: Yes, Grafoil will work chemically, but you will need to handle its mechanical
limitations.
Grafoil (flexible exfoliated graphite) is chemically inert, highly conductive in-plane, and completely
resistant to acidic, neutral, or alkaline electrolytes. Paired with zinc, it functions as a carbon cathode
for hydrogen evolution (or dissolved oxygen reduction), producing an open-circuit voltage around
1.2 V to 1.4 V.
Practical Considerations for a Trough Setup
Mechanical Rigidity: Standard trough cells (like the Cruickshank design) rely on stiff plates
slotted into partition grooves to separate compartments. Grafoil is soft and will flop or tear
under the weight of sloshing electrolyte. It works best if laminated or mechanically clamped to
a rigid, non-conductive backing (e.g., acrylic, 3D-printed frames, or thin plastic sheet).
Bipolar Partitioning (If Building a Series Trough): In a traditional trough battery, the
partition itself is a bipolar plate (zinc on one side, copper on the other). If you want the plate to
act as the watertight divider between cells:
Grafoil is slightly permeable through its thickness if uncompressed, but dense sheets
can work.
Joining zinc directly to Grafoil requires mechanical clamping or a conductive contact
(soldering to graphite is not possible without specialized plating). Clamping a sheet of
Grafoil flat against a zinc plate creates a simple, low-resistance bipolar divider.
Electrical Termination: Since you cannot solder directly to Grafoil, use wide-area
mechanical clamps (like plastic clips over a metal contact strip above the waterline) to prevent
H  SO2 4 NaCl
NH  Cl4
H  SO2 4
H  SO2 4 NaCl
C + MnO  
2 15–20% NH Cl4
ZnCl
 
2
H  
2
NaCl Na  SO2 4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 2/92
tearing the foil while drawing current.
Surface Area & Polarization: Grafoil’s microscopic surface roughness actually gives it an
advantage over polished copper sheet, providing slightly more active surface area for
hydrogen bubble nucleation and release.
User prompt: Does the copper sheet evolve hydrogen in NaCl vs zinc?
Response: In a neutral NaCl solution, copper primarily reduces dissolved oxygen rather than
evolving hydrogen under open-circuit and light-load conditions.
Hydrogen evolution can occur, but only under specific high-current or deoxygenated conditions.
1. Open-Circuit and Normal Discharge (Oxygen Reduction) In aerated neutral saltwater (pH 
), the thermodynamically and kinetically favored cathodic reaction on copper is the Oxygen
Reduction Reaction (ORR):
Paired with zinc oxidation at the anode ( , ), this yields a
theoretical cell voltage of roughly 1.16 V. Under standard conditions, no gas bubbles form at the
copper plate; current is sustained entirely by dissolved oxygen diffusing to the copper surface.
2. Heavy Load / Short-Circuit (Hydrogen Evolution) If the cell is short-circuited or placed under a
heavy electrical load, the demand for electrons quickly outpaces the rate of dissolved oxygen
diffusion through the electrolyte (the mass-transport limit).
When the potential of the copper electrode polarizes down below the hydrogen equilibrium potential
at pH 7 ( ), plus copper's hydrogen overpotential, water reduction takes
over:
Under these conditions, you will observe tiny hydrogen bubbles nucleating and clinging to the
copper plate.
Why NaCl Differs from Acid Electrolytes
In Dilute Acid (e.g., ): High concentration of hydronium ions ( ) means hydrogen
evolution happens immediately and vigorously upon load ( ).
In Neutral : The extremely low  concentration ( ) makes proton reduction
negligible. Current relies on dissolved  (no bubbling) until the cathode potential is pulled
low enough to directly split neutral water molecules.
User prompt: Would copper mesh work in a zn cu cell?
≈
7
O  +2 2H O +2 4e →− 4OH (E =− ∘ +0.401 V vs. SHE at pH 7)
Zn → Zn +2+ 2e− E =∘ −0.763 V
E = −0.414 V vs. SHE
2H  O +2 2e →− H  ↑2 +2OH−
H  SO  
2 4 H+
2H ++ 2e →− H  
2
NaCl H+ 10  M−7
O  
2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 3/92
Response: Yes, copper mesh will work—and in many ways, it will outperform a solid copper
sheet.
Using a mesh electrode offers distinct electrochemical advantages depending on the electrolyte
and load conditions:
Key Advantages
Higher Active Surface Area: Fine mesh significantly increases the true electrochemically
active surface area (ECSA) per unit of frontal area compared to a flat sheet.
Better Oxygen Access in Neutral Brine ( ): Since the primary cathodic reaction in
neutral salt solution is dissolved oxygen reduction ( ), mass
transport of  to the electrode is the main bottleneck. The openings in a mesh allow
convection and faster electrolyte circulation, raising the limiting current density before the cell
polarizes.
Improved Bubble Detachment in Acid ( ): If operated in dilute acid or under heavy
loads where hydrogen evolution occurs ( ), gas bubbles escape more
easily through the apertures rather than forming a continuous insulating film across a flat
plate.
Practical Trade-offs in a Trough Setup
Structural Rigidity: Fine copper wire cloth or woven mesh will sag in liquid. It needs to be
folded, stretched across a non-conductive carrier frame, or made from a thicker expanded
copper mesh to stay flat and avoid shorting against the zinc anode.
Bipolar Partitioning: In a classic Cruickshank-style trough where each divider is a solid,
fluid-tight bipolar plate (zinc on one side, copper on the other), mesh cannot serve as the
watertight partition wall on its own. You would need to mount the mesh against a solid backing
plate or use a single-fluid immersion trough design with separate, suspended electrodes.
User prompt: More surface area than a solid foil? Maybe a double or triple layer.
Response: Yes, fine copper mesh generally provides significantly more true
electrochemically active surface area than flat foil, and multi-layering can push that area
even higher.
A quick geometric comparison clarifies the surface area multiplier and how multiple layers perform:
Flat Foil vs. Woven Mesh Area
For a flat square sheet of side length  submerged on both sides:
NaCl
O  +2 2H  O +2 4e →− 4OH−
O  
2
H
 
SO
 
2 4
2H ++ 2e →− H  
2
L
Area  =foil 2L2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 4/92
For a square wire mesh of side length , wire diameter , and mesh count  (wires per unit
length):
The total wire length in one direction is .
Accounting for both warp and weft wires: .
Approximating each wire as a cylinder (surface area per length ):
Taking the ratio of mesh surface area to flat foil area:
Open Area vs. Wire Area: The product  is the fraction of the linear dimension blocked
by wire. For typical plain weave meshes,  is often between  and .
Area Factor: Multiplying by  gives an area ratio typically between  and 
compared to a smooth flat foil of the same footprint.
Micro-Roughness: Drawn wire also possesses micro-scale surface roughness and
curvature, promoting better fluid contact and bubble release.
Layering Multiple Mesh Sheets (Double/Triple Layer)
Stacking 2 or 3 layers multiplies the solid surface area by  or , but electrochemical utility
depends heavily on mass transport and spacing:
In Neutral  (Oxygen Diffusion-Limited):
If layers are tightly compressed together, the inner surfaces become starved of
dissolved , causing a "shadowing" effect where the interior layers contribute very little
current.
Leaving a slight gap (even 0.5–1 mm) or using a looser open mesh allows natural
buoyant convection of electrolyte, ensuring all layers see fresh dissolved oxygen.
In Acid (Hydrogen Evolution):
Extra layers lower the true local current density ( ), which directly reduces the
activation overpotential required to evolve .
The open apertures provide clear release paths for gas bubbles to escape upwards
instead of getting trapped between layers.
To maximize current in a static bath, loosely tacking 2–3 layers together with spot crimps (or folding
an expanded mesh into an accordion) provides high surface area while keeping the structure open
L d n
nL × L = nL2
Total wire length = 2nL2
= πd
Area  ≈mesh 2πndL2
Ratio =  =2L2
2πndL2
πnd
n ⋅ d
n ⋅ d 0.35 0.60
π 1.1× 1.9×
2× 3×
NaCl
O  
2
i = I/A
H  
2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 5/92
to fluid flow.
User prompt: I assume these things will work better if the gap between the zinc and the copper on
the next bipolar plate is as small as possible?
Response: Up to a point, yes—reducing the inter-electrode gap lowers the internal
electrolyte resistance, but going too narrow introduces severe mass-transport and clogging
bottlenecks.
In electrochemical cells, cell performance is a balance between ohmic (IR) drop and fluid/mass
transport dynamics.
The Primary Benefit: Lower Ohmic Resistance (  Drop)
The bulk resistance of the electrolyte between the zinc and copper plates is:
 = distance between plates (gap)
 = ionic conductivity of the electrolyte
 = plate area
Halving the distance  cuts the electrolyte’s contribution to internal resistance directly in half, giving
a flatter discharge curve and higher usable current under load.
The Trade-offs & Practical Lower Limits
If the gap is made too narrow (e.g., less than 2–3 mm in a static, unpumped trough), several
negative effects quickly overcome the ohmic advantage:
Precipitation & Clogging (In Neutral ):
Zinc oxidizes to , while the cathode generates hydroxide ions ( ).
In neutral brine without strong flow, these ions meet in the bulk gap and precipitate as
insoluble zinc hydroxide / oxychloride (  / ).
In an ultra-narrow gap, this white sludge cannot settle out to the bottom of the trough,
bridging the gap, choking ion transport, and causing localized high-resistance dead
zones.
Bubble Trapping (In Acid / High-Current Conditions):
If hydrogen gas bubbles evolve on the cathode, they need room to rise and detach via
buoyancy.
IR
R  =electrolyte
 =A
ρ ⋅ d
 
κ ⋅ A
d
d
κ
A
d
NaCl
Zn2+ OH−
Zn(OH)  
2 Zn  (OH)  Cl  ⋅5 8 2 H  O2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 6/92
In very tight gaps, capillary forces hold bubbles between the plates. This gas void
fraction displaces conductive electrolyte with insulating gas, drastically increasing the
effective electrical resistance.
Oxygen Diffusion Stagnation (In Neutral Brine):
Since the cathode depends on dissolved , it relies on density-driven natural
convection to bring fresh electrolyte into the space between the plates. A tight gap
chokes this convective flow.
Mechanical Shorting:
Zinc anodes corrode unevenly and can shed small metallic flakes, while thin cathode
foils or mesh can warp. A minimal gap increases the risk of direct physical short circuits.
Practical Rule of Thumb
Static (Unstirred) Trough: A spacing of 4 mm to 8 mm (roughly 3/16" to 5/16") typically hits
the sweet spot—narrow enough to keep  drop reasonable in conductive brine/acid, but
wide enough for natural convection, bubble release, and sediment clearance.
Forced Circulation: If electrolyte is actively pumped or stirred through the trough, the gap
can safely drop down to 1 mm to 2 mm.
User prompt: What limits the capacity of a zinc copper cell?
Response: In a primary zinc-copper cell, capacity (total milliamp-hours, , delivered before the
voltage collapses) is almost never limited by the initial mass of metallic zinc. Instead, it is governed
by electrolyte volume, chemical precipitation, self-discharge, and cathode mass-transport
limits.
Primary Limiting Factors
1. Electrolyte Depletion and Solution Saturation
Neutral  / Brine: As zinc dissolves ( ) and the cathode
generates hydroxide ( ), insoluble zinc hydroxide and zinc oxychlorides (
) precipitate out. Once the local electrolyte is depleted of
available counter-ions or choked with precipitate, ionic conductivity plummets and the
cell dies long before the zinc plate is consumed.
Dilute Acid ( ): Capacity is directly limited by the total moles of hydronium ions (
). For every mole of zinc oxidized, 2 moles of  are consumed to evolve hydrogen
gas. When the acid is neutralized to a neutral zinc sulfate solution, the cell voltage drops
sharply.
2. Zinc Passivation (Fouling of the Anode)
O  
2
IR
mAh
NaCl Zn → Zn +2+ 2e−
OH−
Zn  (OH)  Cl  ⋅5 8 2 H  O2
H  SO  
2 4
H+ H+
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 7/92
In static electrolytes, dissolved  ions accumulate directly at the anode surface
faster than they can diffuse away.
The local pH rises, forming an adherent, non-conductive crust of  / 
across the anode face. This passivation layer blocks further electrochemical dissolution
of the underlying metal, causing an apparent "dead cell" even with substantial zinc
remaining.
3. Open-Circuit Parasitic Self-Discharge
Zinc is thermodynamically unstable in aqueous electrolytes. Even with no external load
connected, local galvanic micro-cells form on the zinc surface (spurred by trace iron,
lead, or copper impurities in the sheet), directly evolving hydrogen gas:
In acid, this corrosion can consume the entire zinc anode in hours to days without
delivering useful work to the external circuit. (Historically, this was mitigated by
amalgamating the zinc with mercury).
4. Cathode Polarization & Dissolved Oxygen Starvation (in Neutral Salt)
If the cell relies on the oxygen reduction reaction ( ), it
delivers continuous current only as fast as atmospheric  can dissolve and diffuse to
the copper plate.
If discharged at a rate faster than ambient replenishment, the cathode polarizes into
deep water reduction, drastically lowering cell operating voltage and usable power
output.
Theoretical vs. Practical Limits
Factor Theoretical Limit Practical Trough Limit
Zinc Metal Mass Rarely achieved (typically 
utilization before fouling)
Dilute Acid (
)
Governs runtime entirely unless fresh
acid is added
Neutral Brine Limited by  solubility (
)
Rate-limited by ambient diffusion;
choked by  sludge
In practice, a trough cell running on a single charge of static electrolyte runs out of usable liquid
capacity (acid consumed or brine passivated by sludge) long before the metal plates are physically
consumed.
Zn2+
ZnO Zn(OH)  
2
Zn + 2H →+ Zn +2+ H  ↑2
O  +2 2H  O +2 4e →− 4OH−
O  
2
820 mAh / gram of Zn < 20–30%
1 M H  SO  
2 4
≈ 53.6 Ah / liter
O
 
2 ≈
8 mg/L Zn(OH)  
2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 8/92
User prompt: How stiff is a 1.2 mm or 1 mm sheet of copper?
Response: A 1.0 mm to 1.2 mm sheet of copper is rigid and self-supporting at small-to-
medium spans (like individual battery plates), but can still be bent cleanly by hand over a
sharp edge or using hand tools.
Tactile Feel & Rigidity
1.0 mm (~18–19 AWG / ~2.9 lb/sq ft): Feels substantial—similar in thickness to a standard
credit card (~0.76 mm) or a US dime (1.35 mm). It will not flop, droop, or sag under its own
weight. You cannot easily flex a 4"  4" plate with your fingers alone, though a long strip can
be bent with firm two-handed leverage.
1.2 mm (~16–17 AWG / ~3.5 lb/sq ft): Visibly stiffer. Because flexural rigidity scales with the
cube of thickness ( ), a 1.2 mm sheet is roughly  stiffer against bending than
a 1.0 mm sheet of the same alloy and temper:
The Role of Temper (Hardness)
How "stiff" the sheet feels in practice depends heavily on whether it is annealed (soft) or cold-rolled
(hard):
Soft / Annealed (O60): Flexes easily under deliberate hand pressure. Once bent, it takes a
permanent set with virtually zero springback. It stays flat if undisturbed, but drops into grooves
or clamps without fighting you.
Half-Hard (H02) or Hard (H04): Significantly higher yield strength. It resists incidental dings
and bending, springs back elastically against light loads, and feels noticeably more rigid when
handled.
Suitability for a Trough Battery Divider
For a DIY trough cell:
Slotting into Grooves: 1.0 mm to 1.2 mm is a sweet spot. It is rigid enough to slide into
slotted side-wall guides and compress against a gasket or beeswax/pitch seal without
buckling under fluid pressure.
Cutting & Working: It can be cut with heavy hand shears, a throatless shear, or a metal-
cutting blade on a saw. It bends crisply in a vise or sheet metal brake without tearing.
Sources
1. K-Factor for Copper: C110 Bend Allowance & Chart - Sheet Metal Fabrication
×
D ∝ t3 1.73×
 =(1.0
1.2 )
3
1.728
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 9/92
User prompt: In copper, what’s the difference between HO2 temper and soft temper?
Response: The difference between Soft (Annealed / O-temper) and H02 (Half-Hard) copper
comes down to cold working (work hardening) and heat treatment, which drastically alters yield
strength, stiffness to permanent bending, and formability while leaving electrical conductivity
virtually unchanged.
Key Mechanical Differences (C11000 / Electrolytic Tough Pitch Copper)
Property
Soft /
Annealed
(O60)
Half-Hard (H02) Impact on Workshop Use
Yield Strength ~70 MPa (10
ksi)
~250–290 MPa
(36–42 ksi)
~3.5–4× higher in H02; resists
permanent bending under hand
pressure.
Tensile Strength ~220 MPa (32
ksi)
~290–340 MPa
(42–49 ksi)
H02 supports higher ultimate
mechanical loads before tearing.
Elongation at
Break 40% – 50% 10% – 20%
Soft copper stretches significantly
before failing; ideal for deep drawing or
flanging.
Hardness
(Rockwell F) ~40–45 HRF ~75–85 HRF H02 resists surface scratches,
indentation, and edge burring.
Springback Virtually zero Moderate H02 "fights back" slightly when bent;
soft stays exactly where you push it.
Electrical
Conductivity
100–101%
IACS
~98–100%
IACS
Negligible difference (~1–2% drop due
to crystal dislocations in H02).
How They Behave in the Shop
Soft (Annealed): Dead-soft and pliable. If you bend a sheet over a 90° corner, it forms with
very little force and retains the exact profile without springing back. However, thin sheets will
easily take accidental dings, warp when handled roughly, and may "potato-chip" if you try to
cut them with hand snips.
H02 (Half-Hard): Produced by cold rolling the copper to reduce its thickness by roughly 20%
after annealing. It feels springy and rigid. It resists accidental deformation, slides cleanly into
tight partition slots without bowing, and maintains flat faces under moderate pressure. It can
still be bent to 90° over a radius, but requires more bending force and exhibits slight
springback.
Annealing & Work Hardening Copper switches between these states readily. Bending,
hammering, or rolling soft copper work-hardens it toward H02/H04. Heating H02 copper with a
torch to a dull red (~500–600°C) and quenching in water instantly returns it to dead-soft temper.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 10/92
User prompt: What about 101 alloy vs 110
Response: The primary difference between Alloy 101 (OFE - Oxygen-Free Electronic) and Alloy
110 (ETP - Electrolytic Tough Pitch) is purity and oxygen content, which impacts high-
temperature processing and hydrogen embrittlement rather than room-temperature electrical
performance.
Key Chemical & Physical Differences
Property C11000 (110 ETP) C10100 (101 OFE) Practical Impact
Purity 99.90% Cu (min) 99.99% Cu (min) 101 is the highest-purity
standard commercial copper.
Oxygen Content 200 to 400 ppm
(0.02–0.04%) < 5 ppm (0.0005%)
110 contains microscopic
cuprous oxide ( )
particles; 101 is truly oxygen-
free.
Electrical
Conductivity
100% to 101.5%
IACS 101% to 102% IACS
Negligible difference for
power and electrochemical
circuits.
Hydrogen
Embrittlement
Resistance
Poor (prone to
cracking if heated
in reducing gas)
Immune
101 can be torch-brazed or
annealed in
hydrogen/reducing flames
safely.
Cost &
Availability
Standard
commercial grade;
low cost,
universally
stocked.
Premium specialty
grade; significantly
more expensive and
harder to find.
110 represents >90% of all
standard copper busbars,
sheet, and pipe.
When the Difference Matters
1. Hydrogen Embrittlement (The Main Engineering Factor):
In 110 ETP, dissolved oxygen forms tiny  inclusions at grain boundaries. If 110 is
heated above ~370°C (700°F) in an atmosphere containing hydrogen or reducing gases
(such as a rich oxy-fuel torch flame), hydrogen diffuses into the metal, reacts with the
oxide to form high-pressure steam ( ), and causes
microscopic grain-boundary cracking and brittleness.
101 OFE has virtually no oxygen, making it completely immune to hydrogen
embrittlement during high-temperature brazing, welding, or vacuum-furnace operations.
2. Ultra-High Vacuum (UHV) & Specialized Electronics:
Cu  O2
Cu
 
O2
Cu  O +2 H  →2 2Cu + H  O2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 11/92
101 OFE is specified for particle accelerators, semiconductor tools, and vacuum tubes
because it resists outgassing when baked under hard vacuum.
Practical Verdict for Battery Cells and Shop Work
For battery plates, electrochemical cells, busbars, and general DIY fabrication:
C110 (ETP) is the standard, economical choice. Its electrical conductivity is essentially
identical to 101, and it solders, cuts, and bends perfectly at room temperature.
C101 (OFE) offers no functional electrochemical or electrical advantage in an ambient
aqueous cell, and is only worth sourcing if you plan on high-temperature furnace brazing in a
reducing atmosphere or building ultra-high vacuum equipment.
User prompt: Hmm, so with the materials that I have I really need something stiff that can be sealed
around the edges. And be able to fasten the zinc and copper to it. Doesn’t have to be conductive
but that would be a bonus. If I printed a trough with solid dividers and left slots on either side that
the foil could slide into that would work. I have some nickel strips that could be bent over the top of
the dividers to connect the metal on both sides.
Response: That is a solid, clean mechanical approach. Using solid printed partition walls and
running the electrical connection over the top bypasses the biggest headache of historic
Cruickshank troughs: trying to make a watertight liquid seal around a metal sheet passing through
the divider.
Design & Mechanical Details to Consider
Watertight Solid Dividers:
To guarantee cell-to-cell isolation with 3D-printed walls, use at least 4–6 solid
perimeter perimeters (walls) and ~100% infill (or concentric top/bottom layers) for the
partition bulkheads. This eliminates microscopic pinhole porosity between extrusion
paths that could cause internal ionic "short circuits" or electrolyte weeping across cells.
A slight draft angle or radius at the base of the slot channels will prevent stress cracking
when sliding foils in.
Top-Bridge Contact Geometry (The Nickel Strap):
Nickel strip (like 0.15 mm or 0.2 mm battery tab strip) is ductile and bends easily into a
tight "U" or "saddle" clip over the divider rim.
Dry vs. Wet Termination: Keep the mechanical junction between the nickel strap and
the foil above the electrolyte waterline. If the copper-nickel or zinc-nickel physical
interface gets submerged in brine/acid, local galvanic micro-cells will form right at the
joint, causing premature corrosion or contact resistance spikes.
Clamping Pressure: A simple 3D-printed friction-fit clip or a printed screw clamp
slipping over the top edge will hold the nickel strap firmly pressed against the copper foil
on one side and the zinc sheet on the other.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 12/92
Slotted Retention Rails:
Integrate vertical channels (e.g., 1.5 mm wide  1.5 mm deep) along the inside face of
each cell wall.
This holds the thin foils/Grafoil flat and maintains an exact, uniform gap (e.g., 5–6 mm)
across the full face without bowing toward each other.
Leaving a 5–10 mm clearance zone at the bottom of the slots creates a collection sump
where precipitate (  sludge or zinc debris) can settle without shorting the
plates or clogging the active surface.
Material Selection:
PETG or ABS/ASA are ideal for electrolyte troughs—they resist dilute acids, salts, and
zinc chloride without swelling or hydrolyzing. Standard PLA works fine for temporary
neutral  testing, but can slowly embrittle or creep over time under sustained liquid
exposure.
User prompt: Were sumps a part of historical trough cells?
Response: No, early Cruickshank-style trough cells did not have sumps.
In William Cruickshank’s original 1800/1802 design, the metal plates themselves served as the
physical bulkheads dividing the long wooden box into individual liquid compartments.
How Historical Trough Cells Were Built
Plates Reached the Floor: Square bimetallic pairs (a zinc plate and copper plate soldered
back-to-back) were slid into vertical grooves cut along the wood sides and bottom, then
sealed directly into the wood using a resinous cement (typically a mixture of pitch, rosin, and
beeswax or shellac).
No Under-Plate Clearance: Because the plates had to create a watertight seal from top to
bottom, there was no continuous cavity or clearance underneath the electrodes. Sediment
accumulated directly on the floor between the plates.
The Evolution of the "Plunge" and Suspended Cell
The lack of a sump, combined with rapid plate fouling and the inability to stop parasitic zinc
corrosion when not in use, quickly proved to be the trough's biggest operational flaw. This led
directly to redesigns:
The Babington / Wollaston "Plunge" Battery (c. 1815): William Babington and William
Hyde Wollaston replaced the bimetallic partition design. They used porcelain or earthenware
troughs with fixed, solid dividers, suspending the zinc and copper plates from a wooden
beam above the trough.
Accidental Sumps: This allowed the experimenter to:
×
Zn(OH)  
2
NaCl
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 13/92
1. Lift the plates out entirely when the battery was idle to stop acid corrosion.
2. Leave open space beneath the suspended plates where sediment and falling sludge
could settle without clogging the active faces or causing bridging shorts.
By the mid-to-late 19th century—culminating in flooded lead-acid designs (like Gaston Planté and
Camille Faure's cells)—dedicated sediment spaces / mud ribs at the bottom of the container
became standard engineering practice to keep flaked oxide debris from bridging the plates.
Sources
1. All you need to know about batteries - Borregaard
User prompt: What are pitch and rosin? I know what beeswax is
Response: Rosin and pitch are traditional resinous binders derived from pine trees (or fossil fuels),
historically used as the standard waterproof, acid-resistant sealants and adhesives before modern
synthetic polymers and silicones existed.
What is Rosin (Colophony)?
Rosin is the solid, amber-colored natural resin left behind after distilling liquid pine oleoresin to
extract volatile turpentine (spirits of turpentine).
Properties: It is hard, brittle, translucent, and easily crushed into a fine powder. It melts at
roughly 70°C to 100°C (160°F to 212°F) into a sticky liquid.
Chemical Nature: Primarily composed of abietic acid and related diterpene resin acids. It is
insoluble in water and highly resistant to acids, but dissolves in alcohols, acetone, and hot
oils.
Familiar Modern Uses: The solid amber cake used on violin bows, the grip powder used by
baseball pitchers and gymnasts, and the active flux core inside electrical solder wire.
What is Pitch?
Pitch is a thick, dark, viscous or solid residue obtained by heavily boiling down or pyrolyzing organic
tars. Historically, there were two main types:
Pine Pitch (Wood Pitch / Brewer's Pitch): Made by boiling down pine tar (the charred,
smoky sap extracted from kiln-burning pine wood stumps). Boiling drives off the volatile oils
until a thick, black, tarry waterproof glue remains.
Coal-Tar / Petroleum Pitch (Bitumen / Asphalt): The heavy, black aromatic residue left after
the distillation of coal tar or crude oil.
Properties: Pitch is much darker, more flexible, and more tenacious than pure rosin. It
softens with heat and cools to a tough, sticky, impermeable black sealant.
Historical Uses: Caulking the hulls of wooden sailing ships ("paying the seams"), lining
wooden beer casks (brewer's pitch), and waterproofing roofs and pipes.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 14/92
Why Early Scientists Combined Them with Beeswax
In early electrochemical apparatus like Cruickshank troughs and Leyden jars, neither ingredient
was used alone:
Pure Rosin is too brittle on its own—it cracks as wood expands or metal plates flex.
Pure Beeswax is too soft and has a low melting point (~62°C–64°C).
Pure Pitch can be too soft and tacky at room temperature.
By melting rosin, pitch (or beeswax), and an inert mineral filler (like brick dust, plaster of
Paris, or red ochre) together, 18th- and 19th-century builders created "Philosophical Cement"
(or electrical cement). The rosin provided adhesion to wood and metal, the beeswax/pitch added
plasticity to resist thermal shock cracking, and the powder filler gave it compressive bulk to fill gaps
permanently without shrinking.
User prompt: Isn’t shellac something that was available in the 19th century?
Response: Yes, shellac was widely available and heavily used throughout the 19th century.
It was one of the most important natural insulating and binding materials of the early electrical era,
imported in massive quantities from India by the British East India Company.
What Shellac Is
Unlike pine-derived rosin or pitch, shellac is an animal byproduct. It is a natural resin secreted by
the female lac bug (Kerria lacca) on trees in India and Southeast Asia. The crusty resin harvest
("sticklac") was washed, refined, and stretched into thin sheets that were broken into flakes.
How 19th-Century Scientists Used Shellac
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 15/92
Shellac had outstanding dielectric strength, moisture resistance, and chemical stability, making it a
staple across laboratories:
Electrical Insulation & Wire Enamel: Dissolved in high-proof ethanol ("spirits of wine"),
liquid shellac was painted onto copper wires, electroscope rods, and glass friction machines
to prevent high-voltage charge leakage.
Sealing Wax & Cements: Combined with Venice turpentine and pigments (like vermilion),
shellac was the primary ingredient in high-grade sealing wax and rigid lab cements used to
seal glass tubes, Leyden jars, and galvanic apparatus.
Waterproofing Troughs & Woodwork: Instrument makers painted the interior wooden
frames of early batteries, galvanometer housings, and coil bobbins with shellac varnish to
prevent acid moisture from soaking into the grain.
Shellac vs. Rosin/Pitch for Trough Batteries
While shellac was widely available, builders usually chose rosin-and-pitch cements over shellac
for sealing trough partitions:
Property Pine Rosin / Pitch Cements Shellac
Gap-Filling
Bulk
Excellent. Melts into a thick, cheap,
gap-filling mastic that cools solid in
minutes.
Poor. Thicker layers shrink and crack
as solvent evaporates.
Cost in 1800 Extremely cheap; locally sourced from
pine forestry.
Imported luxury commodity;
substantially more expensive.
Brittleness Easily plasticized with beeswax or
pine pitch to resist vibration.
Hard and glass-brittle when melted
without extensive plasticizers.
Acid
Resistance
Impervious to dilute  and
.
Resistant to dilute acid, but can soften
slowly in some alkaline environments.
19th-century builders typically used shellac as a painted insulating varnish or fine glass-to-
metal sealant, while reserving cheap, heavy-bodied rosin/pitch mixtures for caulking deep
grooves and large wooden battery troughs.
User prompt: What’s a recipe for 19th century battery cement?
Response: The standard 19th-century formula used by instrument makers and natural philosophers
to seal trough partitions, galvanic apparatus, and Leyden jars was known as Electrical Cement (or
Philosophical Cement).
Standard Electrical / Battery Cement (By Weight)
5 parts Pine Rosin (Colophony) — The adhesive binder.
H  SO  
2 4
HNO
 
3
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 16/92
1 part Beeswax — The plasticizer (prevents the rosin from cracking).
1 part Inert Powder Filler (historically Red Ochre, finely ground Plaster of Paris, or Brick
Dust) — Adds structural body and reduces thermal shrinkage.
Alternate Historic Variations
For High Flexibility / Vibration Resistance (Pitch Heavy):
4 parts Rosin
1 part Pine Pitch
1 part Beeswax
1 to 2 parts Finely sifted brick dust or dry Spanish red oxide.
For Extra Adhesion to Smooth Surfaces (Glass / Smooth Metal):
Replace half of the beeswax with Canada balsam or Venice turpentine.
Preparation & Application Protocol
1. Dry the Filler: Heat the red ochre, brick dust, or plaster of Paris in a dry pan or oven to drive
off all residual moisture. (If damp powder is added to hot molten rosin, it will froth violently and
trap air pockets).
2. Melt the Base: Melt the rosin and beeswax together over low heat (ideally in a double boiler
or controlled heat bath around 100°C–120°C / 212°F–250°F) until completely liquefied.
3. Incorporate the Powder: Slowly stir in the warm, dried powder filler until the mixture is
smooth and completely homogenous.
4. Application:
Warm the wooden trough grooves and metal plates slightly before applying the cement.
If applied to freezing-cold metal, the mastic quenches instantly and fails to wet the
surface properly.
Pour or trowel the hot cement into the slots and press the divider plates in firmly.
Smooth the joint fillets using a heated iron spatula or hot metal rod. The cement sets
completely rigid as soon as it cools to room temperature.
Sources
1. The microscopist : a manual of microscopy and compendium of the microscopic science :
micro-minerology, micro-chemistry, biology - Internet Archive
User prompt: Brick dust is a ridiculous price because it is used in ceremonies of some kind. Red
ochre comes back as paint, or bags of iron oxide. It is iron oxide plus silica and clay. When I search
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 17/92
for clay powder I get bentonite, so I’m wondering if I could use crushed bentonite kitty litter. Plaster
of Paris would be next cheapest. I have kitty litter
Response: Yes, crushed bentonite kitty litter will work, but Plaster of Paris is the superior,
easier, and historically authentic choice.
Using Bentonite Kitty Litter: Pros & Pitfalls
If using plain, unscented, additive-free clay litter:
The Swelling Problem: Bentonite is a smectite clay engineered to swell significantly when in
contact with water. In a hydrophobic matrix of molten rosin and beeswax, the individual clay
particles are largely encapsulated. However, if micro-cracks form or edge boundaries are
exposed to aqueous battery electrolyte, bentonite can absorb water, swell, and compromise
the seal over time.
Moisture Foaming: Raw bentonite holds bound atmospheric moisture. If added directly to
molten rosin (~120°C), it will cause violent boiling and foaming, trapping micro-voids in the
cement. It must be baked bone-dry in an oven at 150°C (300°F) for an hour before mixing.
Grinding Effort: Uncrushed litter grains are too coarse (aggregates will prevent the cement
from packing tightly into narrow slots). It must be pulverized to a fine flour using a mortar and
pestle or shop mill.
Why Plaster of Paris is the Better Choice
Plaster of Paris (calcium sulfate hemihydrate) was one of the three primary fillers cited directly in
19th-century electrical manuals (along with red ochre and Spanish whiting):
Ultra-Fine Texture: Already milled to micron-scale particle sizes, allowing the molten cement
to flow into tight joint channels.
Dimensional Stability: Does not swell or expand in the presence of water or acidic/saline
electrolytes once locked into the wax/resin binder.
Thermal Shock Resistance: Adds substantial compressive strength and prevents the rosin
from shrinking and pulling away from metal plates as it cools.
Cost: Available at any hardware or craft store for a few dollars.
Other Cheap, Readily Available Fillers
If looking around the shop or local garden/hardware center, several everyday minerals act as inert
fillers for electrical cement:
Chalk / Whiting / Agricultural Limestone (Calcium Carbonate): Historically called "Spanish
Whiting." Non-swelling, cheap, and very fine.
Play Sand / Quartz Silica Flour: Extremely inert and impervious to all battery acids, though
harder to find in fine flour grades.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 18/92
Diatomaceous Earth: Very light, non-reactive, and already an ultra-fine powder (bake dry
before use).
Baking the filler dry before stirring it into the molten resin is the critical step to prevent bubbling and
ensure a dense, leak-proof seal in the trough.
User prompt: I will use plaster of Paris . What is a Daniel cell?
Response: The Daniell cell is a two-fluid primary electrochemical cell invented in 1836 by British
chemist John Frederic Daniell. It was the first battery to produce a steady, reliable, unvarying direct
current over long periods, making it the workhorse power source of the early telegraph industry.
The Problem It Solved: Cathode Polarization
Earlier single-fluid batteries (like the Voltaic pile and Cruickshank trough) put zinc and copper into
the same acid or salt solution. Under load, hydrogen ions reduced directly on the copper cathode (
), creating an insulating blanket of gas bubbles that caused voltage to collapse
within minutes.
Daniell solved this by eliminating hydrogen gas evolution entirely. Instead of reducing protons,
the cell uses a second electrolyte containing copper ions ( ), so that discharge deposits solid
copper onto the cathode rather than generating gas.
Anatomy & Cell Reactions
A Daniell cell consists of two separate half-cells separated by a porous barrier (an unglazed
earthenware pot or salt bridge) to allow ion transfer while preventing rapid liquid mixing:
Anode (Negative): A zinc plate immersed in dilute zinc sulfate ( ) or dilute sulfuric
acid ( ).
Cathode (Positive): A copper plate immersed in a saturated copper(II) sulfate ( )
solution, often kept saturated with blue bluestone crystals.
Overall Reaction:
The standard open-circuit potential is remarkably stable at . Because of this steady
output, the Daniell cell was historically used as the international reference standard for the
definition of the volt.
The Two Major Historical Configurations
2H ++ 2e →− H  
2
Cu2+
ZnSO  
4
H  SO  
2 4
Zn  →(s) Zn  +(aq)
2+ 2e (E =− ∘ −0.763 V)
CuSO  
4
Cu  +(aq)
2+ 2e →− Cu  (E =(s)
∘ +0.342 V)
Zn  +(s) Cu  →(aq)
2+ Zn  +(aq)
2+ Cu  
(s)
≈ 1.10 V
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 19/92
1. Porous Pot Type (Standard Lab Design): An unglazed ceramic cup sits inside an outer
glass or copper container. One half-cell is placed inside the cup (usually zinc in  /
acid), and the other half-cell occupies the outer vessel (copper in saturated ).
2. Gravity Cell (Crowfoot Cell): Developed by C.F. Varley and J.B. Fuller in the 1850s, this
eliminated the porous pot entirely. A dense, concentrated  solution sits naturally on
the bottom of a glass jar around a copper "leaf" electrode, while a lighter, less dense 
solution floats on top around a claw-shaped zinc "crowfoot" anode. As long as the jar is
undisturbed and drawn under continuous light current, the density boundary prevents copper
ions from reaching the zinc.
User prompt: Can the separator be cast from plaster of Paris?
Response: Yes, cast Plaster of Paris works well as a porous separator, and it has strong
historical precedent. In 1837, British physician Golding Bird developed a famous variant of the
Daniell cell using a cast Plaster of Paris partition instead of an unglazed earthenware pot.
How It Functions Electrochemically
When Plaster of Paris (calcium sulfate hemihydrate) cures with water into gypsum (calcium sulfate
dihydrate), it forms an interlocking, needle-like crystalline matrix ( ).
Microporosity: The space between crystals creates an interconnected network of
microscopic pores that soak up electrolyte, allowing sulfate ( ), zinc ( ), and
sodium/hydronium ions to migrate freely.
Diffusion Barrier: The tortuous pore structure slows bulk hydraulic mixing and diffusion,
keeping the dark blue  ions from reaching the zinc anode while the cell is active.
Practical Casting Tips for a DIY Cell
Target Thickness (3 mm to 6 mm):
Too thin (<2 mm): Very fragile and prone to cracking under water pressure.
Too thick (>8–10 mm): Drastically increases internal ionic resistance (  drop),
reducing usable output current.
A 3–5 mm cast plate hits the sweet spot for durability versus internal resistance.
Water-to-Plaster Ratio: Mix slightly wet (around a 1:1 to 1.2:1 water-to-plaster weight ratio).
Using adequate water ensures open, connected porosity throughout the cured block rather
than an ultra-dense, impermeable matrix.
Pre-soaking Before Use: Never place a dry plaster diaphragm into active battery
electrolytes. Pre-soak the cured plaster partition in clean water or dilute salt/zinc
solution for a few hours first. If installed dry, it will greedily wick up the copper sulfate
ZnSO  
4
CuSO  
4
CuSO  
4
ZnSO
 
4
CaSO  ⋅4 2H  O2
SO  
4
2− Zn2+
Cu2+
IR
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 20/92
solution by capillary action, drawing copper ions directly through the pores to the other side
before the cell even starts running.
Mechanical Reinforcement: Plaster is brittle in thin sheets. Casting it over a piece of open
plastic mesh, coarse cheesecloth, or fiberglass drywall tape embedded in the center gives it
tensile strength and prevents catastrophic cracking if handled or bumped.
Lifespan Limit: Gypsum is slightly soluble in water (~2 g/L) and softens in strong acids over
time. For neutral salt or dilute sulfate electrolytes, a plaster separator will easily last through
weeks of experimentation, but it is not intended as a permanent multi-year installation like
vitrified earthenware.
Sources
1. History of the battery - Wikipedia
User prompt: The copper cathode could be on the inside of the pot correct? Just wondering about
using copper pipe
Response: Yes, the copper cathode and  solution can be placed on the inside of the
porous cup, but using a copper pipe as the outer vessel is actually the most authentic and
efficient design.
1. Copper on the Inside (Inverted Layout)
Setup: A copper tube or rod sits inside the porous cup filled with , while the outer bath
contains the zinc anode and  (or  / dilute acid).
Electrochemical Function: The cell works normally at ~1.1 V.
Drawback: The interior volume of the porous pot is small. This limits the volume of 
and surface area of the copper cathode, meaning  ions deplete quickly unless you
frequently add solid bluestone crystals into the pot.
2. Copper Pipe as the Outer Vessel (Original 1836 Layout)
John Frederic Daniell’s original patent actually used a copper cylinder/pipe as the container
itself:
Double Duty: A capped copper pipe serves as both the outer container and the active
cathode.
High Surface Area & Low Resistance: The entire inner circumference of the pipe acts as
the cathode, surrounding the central porous cup symmetrically. This maximizes active surface
area and minimizes ionic path length (  drop).
CuSO  
4
CuSO
 
4
ZnSO  
4 NaCl
CuSO  
4
Cu2+
IR
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 21/92
Reservoir Space: The outer space between the pipe and the porous pot leaves plenty of
room for saturated  solution and a perforated shelf of copper sulfate crystals near the
top. As copper plates out, dissolving crystals naturally maintain saturation via density
circulation.
Practical Fabrication Note with Copper Pipe
If using standard copper plumbing pipe (e.g., 1.5" or 2" Type M/L/DWV):
Solder a standard copper end-cap to the bottom (or seal it into a 3D-printed base with
epoxy/resin).
Place the cast plaster separator (or ceramic cup) with the zinc rod in the center.
Fill the outer annulus with  and connect directly to the copper pipe's outer rim for the
positive terminal.
User prompt: Could I spot weld zinc foil to thin copper sheets? Or what is the best way to join the
two together? I have a small spot welder for battery strips. How would it have been done in the 19th
century?
Response: Spot welding zinc foil directly to copper sheet with a standard DIY
pulse/capacitive battery spot welder will generally not work well, but soft soldering is
straightforward, highly effective, and historically authentic.
Why Small Battery Spot Welders Struggle Here
Battery tab spot welders work by passing a brief, intense burst of current through high-resistance
nickel strip to melt it at the contact interface. Joining zinc to copper creates two major physical
hurdles:
High Thermal & Electrical Conductivity: Copper has nearly four times the electrical
conductivity and six times the thermal conductivity of nickel. It shunts the current away and
conducts heat out of the contact point so fast that a low-power DIY welder cannot generate
the localized resistance heat needed to fuse the metals.
Vaporization & Burn-Through: Zinc melts at 419.5°C and boils at 907°C, while copper melts
at 1085°C. By the time enough heat is pumped into the copper to make it weldable, thin zinc
foil will vaporize in a burst of white zinc oxide smoke, blasting a hole straight through the foil
rather than forming a weld nugget.
(If you ever attempt spot welding with zinc, avoid inhaling the fumes, as vaporized zinc causes
metal fume fever).
How It Was Done in the 19th Century
In William Cruickshank’s original 1800–1802 trough batteries, the plates were joined using soft
soldering (tin-lead alloy):
CuSO  
4
CuSO
 
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 22/92
Solder Seam / Lamination: 19th-century builders tinned the copper sheet and zinc plate
using a charcoal-heated copper soldering iron, killed spirits (zinc chloride flux), and common
solder ( ).
Face-to-Face vs. Edge Joining:
In Cruickshank’s design, equal-sized square plates of zinc and copper were soldered
together face-to-face (or sweat-soldered along their perimeter edges) to form a rigid,
solid bimetallic partition.
In Babington/Wollaston plunge batteries, the plates were joined at the top by a small
soldered arch or strip of copper/brass that bent over the wooden suspension bar.
Best Methods for Your Shop
1. Sweat Soldering (Best Electrochemical & Mechanical Bond):
Flux: Use an aggressive flux for zinc (rosin flux is too weak on zinc oxide). Traditional
zinc chloride flux (historically "killed spirits") or a modern liquid water-soluble acid flux
cleans both metals instantly.
Process: Lightly tin the contact edge of the copper sheet with standard solder (
 or lead-free ). Lay the clean zinc foil over it, apply a drop of flux,
and touch the joint with a medium-temperature iron (~250°C–300°C).
Tip: Do not overheat the zinc—solder flows onto zinc very quickly once the oxide is
stripped by flux. Rinse with water afterward to remove flux residue.
2. Mechanical Fastening / Riveting (Fast & Zero Heat):
Use small copper, brass, or aluminum pop rivets or eyelets to crimp the zinc foil and
copper sheet together along the top dry tab.
Applying firm mechanical clamping pressure between clean bare faces provides low
electrical contact resistance without any risk of melting the foil.
3. Nickel-Strap Sandwich (Using Your Spot Welder):
If you want to use your spot welder, you can sandwich the metals: spot weld a nickel
strip to another nickel strip clamped tightly around the foil tab, or use the spot welder to
tack nickel strip directly to thin nickel-plated contact shims rather than welding bare zinc
to bare copper.
User prompt: The method you outlined only joins the plates along one edge?
Response: Yes—and historically, joining only along the edges was standard practice.
In early 19th-century trough batteries, the plates did not need full face-to-face contact to function as
bipolar dividers.
50/50 Sn-Pb
60/40 Sn-Pb Sn-Cu
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 23/92
How 19th-Century Builders Joined Bipolar Pairs
Perimeter/Edge Soldering: Cruickshank and later instrument makers typically placed a
square of zinc and a square of copper back-to-back and ran a bead of solder along the top
and side edges (or just the top and bottom corners).
Why Full Face Lamination Wasn’t Needed:
Low Current Densities: These cells produced small currents (milliamps to a few
hundred milliamps). Because both copper and zinc are excellent electrical conductors,
electrons flow easily from the entire zinc face, through the sheet, to the soldered edge
seam, and back across the copper plate with negligible voltage drop.
Mechanical Flatness: Early rolled or cast metal sheets were rarely optically flat.
Soldering only the edges was much faster, consumed far less tin/lead solder, and
prevented trapped flux pockets between the plates.
Modern DIY: Top-Edge vs. Full-Face Lamination
For a DIY cell, you have three options depending on your design:
Method How It's Done Pros / Cons
Top-Edge Seam /
Strap
Solder or clamp the zinc and
copper together only along the top
tab/rim above the waterline.
Easiest and cleanest. Keeps the
bimetallic joint completely dry,
preventing local galvanic corrosion
at the solder seam.
Edge-Perimeter
Soldering (Historical
Cruickshank)
Run a thin bead of solder along 2–
3 outer edges of the paired plates.
Forms a single rigid plate ready to
slide into trough grooves and seal
with pitch/cement.
Full-Face Sweat
Soldering
Tin the entire back of both sheets,
clamp them in a vise or flat plates,
and heat with a torch until solder
flows across the whole area.
Maximum rigidity and lowest
internal resistance, but requires
significant heat and can easily warp
thin foils or melt zinc.
If you use solid 3D-printed partition walls with separate slots for the zinc and copper, joining them
along the top dry edge via a soldered tab or bent nickel strap is all you need—the electrical
conduction across the top bridge will carry the full current without measurable loss.
User prompt: So clean with flux, melt a bead of solder onto one edge of the copper (inside the
edge?) , then press the zinc on and slowly run a soldering iron across the edge to be joined to melt
the solder
Response: Yes, that is the exact essence of sweat soldering, but with zinc, heat management
and iron placement require one specific technique.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 24/92
Because zinc foil melts at a relatively low temperature (419.5°C) and conducts heat quickly,
pressing a hot iron directly onto the thin zinc face can melt or tear the foil before the solder
underneath flows.
Step-by-Step Technique for Zinc-to-Copper Sweat Soldering
1. Surface Prep & Tinning the Copper:
Clean both metal surfaces with fine abrasive (Scotch-Brite or steel wool) until shiny.
Apply a drop of liquid acid/zinc chloride flux along a 3–5 mm strip near the top edge of
the copper.
Run your iron across that strip with a small amount of solder to create a thin, uniform,
pre-tinned silver band on the copper (keep it flat, avoiding tall lumps).
2. Flux the Zinc:
Clean the mating edge of the zinc foil.
Apply a thin film of flux to the back edge of the zinc (where it will touch the tinned copper
band).
3. Align & Clamp:
Overlap the zinc edge directly onto the tinned copper band.
Hold the pieces firmly in place with a wooden stick, dry scrap wood, or metal tweezers
so they cannot shift during heating.
4. Heat Through the Copper (The Pro Trick):
Apply the soldering iron tip to the thicker copper side (or just adjacent to the zinc
edge on the copper sheet) rather than directly burning through the zinc foil.
Copper will absorb the heat and conduct it through the joint, melting the pre-tinned
solder cushion.
As soon as you see the solder flash/liquefy and wet the seam under the zinc, glide the
iron along the seam and remove the heat immediately.
5. Cool & Rinse:
Keep light pressure on the zinc for 3–5 seconds until the solder solidifies from shiny
liquid to a dull solid.
Rinse thoroughly with warm water to wash away all acid flux residue, preventing
white crusty corrosion at the joint later.
User prompt: I suppose the other edges would be held close by the slot. If I do this I would be
aiming for a historical battery. For funsies
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 25/92
Response: Exactly—that is the beauty of the Cruickshank design.
Once the paired pair of plates slides into the side and bottom dados of the wooden trough, the
surrounding electrical cement seals and holds the remaining three edges firmly in place.
How the Assembly Locks Together
1. Top Solder Seam: Joining the zinc and copper along the top rim keeps them electrically
linked, prevents electrolyte from wicking down between the faces, and makes handling the
pair as a single rigid unit easy.
2. Groove Retention: The side and bottom edges slide directly into the kerfs cut across the
floor and walls of the wooden box.
3. Cement Potting: Molten electrical cement (rosin + beeswax + dried Plaster of Paris) is
poured directly into the groove joints. It flows around both metal edges, potting and sealing
the bottom and sides into a continuous, liquid-tight barrier between adjacent cells.
Key Historical Details for Authenticity
Wood Choice: Historically, well-seasoned mahogany, oak, or walnut was preferred because
it resists warping when moist. The entire interior of the wood box was coated in hot
resin/varnish to seal the grain before installing plates.
Plate Orientation: Every pair faces the exact same direction (e.g., Copper  Zinc 
Electrolyte  Copper  Zinc). This puts all the cells in series, adding ~1.0 V to 1.1 V per
compartment.
Terminal Leads: The end plates get heavy copper wire terminals soldered directly to the
exposed end faces, often routed to small brass binding posts or simple wooden side notches.
User prompt: Current delivery would be limited by the area of the plates?
Response: Yes, the maximum current a trough battery can deliver is directly proportional to
the submerged surface area of the plates.
This relationship between plate size, cell count, and electrical output was one of the first major
discoveries of early 19th-century electrochemistry.
Why Surface Area Limits Current
The peak and sustained current delivery are dictated by electrochemical and transport limits that
scale directly with active area ( ):
Ohmic Internal Resistance ( ): The bulk electrolyte resistance of each cell is inversely
proportional to plate area:
→ ∣
∣ →
A
R  
int
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 26/92
Doubling the submerged area halves the cell's internal resistance, which cuts the internal
voltage drop ( ) under load in half.
Limiting Current Density ( ): Electrochemical reactions have an inherent rate limit per
unit area (  in ):
In Neutral Brine ( ): The cathode is throttled by dissolved oxygen diffusion (
). To draw 100 mA without crashing cell voltage into hydrogen
evolution, you physically need  of active copper area.
In Dilute Acid ( ): Hydrogen evolution allows much higher rates (
), but high current densities accelerate zinc surface passivation and
create severe local gas blinding. A larger plate area keeps the local current density low,
delaying polarization.
The Historical "Davy vs. Children" Rules
Early researchers like Humphry Davy and John George Children realized that battery dimensions
dictated what experiments they could run:
Dimension Changed What Increases Historical Demonstration
Increase Number of
Cells ( ) (Many small
plates)
Voltage (
)
Decomposing chemical compounds, making
sparks jump across gaps, giving strong
physiological shocks.
Increase Plate Area ( )
(Few massive plates)
Current (
)
Heating and melting thick platinum or iron wires,
igniting gunpowder, magnetic deflection.
Cruickshank troughs built for general laboratory work typically used plates around 3"  3" (7.5 cm
 7.5 cm) or 4"  4" (10 cm  10 cm), which provided enough surface area to sustain 50–200
mA loads for basic electrolysis and magnetic experiments without collapsing under rapid
polarization.
User prompt: Wait is the active area of copper the area of a single plate or of the entire battery?
Response: It is the area of a single plate (or single cell), NOT the sum of the entire battery.
Because a trough battery connects all its cells in series, every individual cell carries the exact
same total electrical current.
R
 
=cell
 
A
ρ ⋅ d
IR
i  
limit
i = I/A mA/cm2
NaCl ∼
0.1–1.0 mA/cm2
∼ 100–1000 cm2
H  SO  
2 4 ∼
10–50 mA/cm2
N V  =total N ⋅
V
 
cell
A
I  ∝max A
×
× × ×
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 27/92
The Series Circuit Bottleneck
In a series string:
The total current flowing through the circuit must pass through every cell one after
another.
If your trough has 10 cells, and you draw  from the battery terminals, that exact same
 is flowing across Cell 1, Cell 2, Cell 3... all the way to Cell 10.
Therefore, the current density ( ) at the copper surface in each cell is determined
solely by the submerged surface area of that single plate.
   [Cell 1]       [Cell 2]       [Cell 3]
 +-[Cu | Zn]-----[Cu | Zn]-----[Cu | Zn]-+
 |    100 mA         100 mA        100 mA|
 +---------------------------------------+
If the single plate area is , drawing  forces a current density of  on
every single plate. Adding more cells in series increases the total voltage, but it does nothing to
alleviate the current density on any individual plate.
Series vs. Parallel Summary
Battery Configuration Total Voltage Max Current
Capability Determining Factor
Series (Standard Trough) Unchanged (Same
as 1 cell) Area of a single plate
Parallel (Plates wired
side-by-side) (~1.0 V)
Combined total area of
all plates
If you want the battery to supply a higher sustained current without rapidly polarising, you must
physically increase the width and height of the individual plates, rather than just adding more
compartments to the trough.
User prompt: So a 4” x 4” sheet looses some area at the top to stay dry and around the edges. So
let’s say 80 cm^2. Using your numbers above I get just over 80 amps in acid and 88 mA in brine.
That seems wildly different
Response: Taking the current density ranges mentioned earlier:
For brine (0.1 to 1.0 mA/cm²):
100 mA
100 mA
i =  
A
I
25 cm2 100 mA 4 mA/cm2
V  =total N ×
V  
cell
V  =total V  
cell I  =total N × I  
cell
At 1.0 mA/cm ×2 80 cm =2 80 mA
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 28/92
For acid (10 to 50 mA/cm²):
An arithmetic unit conversion slip caused the acid estimate to appear as  instead of
.
Even with the corrected units, the difference between ~80 mA (brine) and ~800 to 4,000 mA (acid)
—a factor of  to —is genuine, and stems directly from the reaction mechanisms:
In Brine (Mass-Transport Limited): The cathode depends on ambient dissolved oxygen (
), which is present only in trace amounts (around 8 mg/L or ). The reaction rate
is strictly bottlenecked by how quickly oxygen molecules physically diffuse through stagnant
water to hit the copper surface.
In Acid (Reactant-Abundant): The cathode reduces hydronium ions ( ), which are present
at enormous concentrations ( , or nearly 10,000 times more concentrated than
dissolved oxygen). Because reactant ions are packed right against the metal surface, current
can flow orders of magnitude faster before becoming diffusion-limited.
User prompt: What are some historical dimensions of Cruikshank cells ?
Response: Historical Cruickshank trough batteries from the early 1800s were built in a few
standardized configurations depending on whether they were intended for high-tension sparks
(many small plates) or high-current chemical deflagration (fewer large plates).
Standard Laboratory Sizes (1800–1810)
The Small / High-Tension Model (Davy's Multi-Cell Troughs):
Plate Size: 1.5"  1.5" to 2"  2" (approx. 3.8 cm to 5.0 cm square).
Cell Count: Typically 50 to 100 pairs in a single trough (often 24" to 36" long).
Inter-Plate Gap (Compartment Width): 0.25" to 0.375" (~6 mm to 9 mm).
Purpose: Built to generate hundreds of volts in series for physiological experiments,
electric arcs, and decomposing salts.
The Standard Medium Laboratory Workhorse:
Plate Size: 3"  3" or 4"  4" (approx. 7.5 cm to 10 cm square).
Cell Count: Usually 20 to 25 pairs per wooden box.
At 1.1 mA/cm ×2 80 cm =2 88 mA
At 10 mA/cm ×2 80 cm =2 800 mA (0.8 A)
At 50 mA/cm ×2 80 cm =2 4000 mA (4.0 A)
80 A
0.8 A to 4 A
10× 50×
O  
2
∼ 0.25 mM
H+
1 M to 2 M
× ×
× ×
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 29/92
Inter-Plate Gap: 0.375" to 0.5" (~9 mm to 13 mm).
Trough Dimensions: Roughly 24" to 30" long, 5" wide, and 4" to 5" deep (internal).
Purpose: The everyday bench standard for electrolysis of water and metal
electrodeposition.
The "Deflagrator" / High-Current Sizes:
Plate Size: 6"  6" to 8"  8" (approx. 15 cm to 20 cm square).
Cell Count: 10 to 20 pairs per trough.
Inter-Plate Gap: 0.5" to 0.75" (~13 mm to 19 mm) to allow sufficient acid volume and
gas venting.
Purpose: Igniting gunpowders, melting thick metal wires, and producing continuous arc
lighting.
Structural Construction Specs
Wood Box Thickness: Typically 0.75" to 1.0" (19 mm to 25 mm) thick seasoned mahogany,
walnut, or oak to prevent warping from acid moisture.
Kerf / Groove Depth: Side and bottom dados were cut 0.125" to 0.187" (3 mm to 5 mm)
deep into the wood walls to seat the bimetallic plates firmly before pouring the resin cement.
Liquid Level: Boxes were filled to within 0.5" to 0.75" (12 mm to 19 mm) of the top rim,
leaving the soldered top edge of the plates dry.
User prompt: What thickness of metal would be used?
Response: In 19th-century Cruickshank troughs, the zinc and copper plates were intentionally
made with unequal thicknesses because they served very different roles:
Zinc Plate (The Sacrificial Anode): 1.5 mm to 3.0 mm (approx. 1/16" to 1/8" / 11 to 16
gauge).
Because zinc is chemically consumed during discharge and constantly dissolves away
into the acid, thin zinc foils would perforate and fail after just a few runs.
A thick zinc plate provided structural rigidity across the wooden groove and enough
sacrificial metal mass to survive multiple cleanings and acid refills before needing
replacement.
Copper Plate (The Insoluble Cathode): 0.5 mm to 1.0 mm (approx. 1/32" to 1/16" / 18 to 24
gauge, historically called "stout sheet copper" or 16–24 oz roofing/brazier copper).
Copper does not dissolve during normal discharge; it merely serves as an electron
conductor and gas evolution substrate.
× ×
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 30/92
It only needed to be thick enough to resist crumpling, stay flat against the zinc, and
provide structural stiffness for the slot seal.
Combined Bipolar Pair Thickness
When sweat-soldered back-to-back, the total paired sandwich was typically 2.0 mm to 4.0 mm
thick (~3/32" to 5/32").
This combined thickness gave the divider enough stiffness to span a 3" to 5" wide trough box
without bowing, allowing standard wood saws of the era to cut a matching ~1/8" (3 mm) kerf into
the trough walls to receive the plate assembly.
Sources
1. "Historic Papers in Electrochemistry"
User prompt: Hey what changes to make a zinc anode part of a rechargeable cell? I have this
niggling memory that we discussed zinc anode batteries before with graphite felt cathodes
Response: To transition zinc from a primary, single-use anode into a truly reversible, rechargeable
electrode, the core electrochemical principle shifts from sacrificial dissolution to a clean cycle of
dissolution on discharge and uniform electrodeposition (plating) on charge:
Making this reversible in practice requires addressing several fundamental failure modes of zinc:
1. The Three Main Hurdles of Rechargeable Zinc
Dendrite Growth: During recharging, zinc ions do not naturally plate back as a smooth, flat
sheet. Instead, electric fields concentrate at microscopic high points, causing tree-like metallic
needles (dendrites) to grow across the separator until they short-circuit the cell.
Shape Change & Mass Redistribution: Zinc dissolves from high-current-density areas
during discharge and replates unevenly (often pooling near the bottom edges of the plate),
causing the electrode to distort and lose active area over multiple cycles.
Hydrogen Evolution During Charge: Zinc’s standard reduction potential ( ) sits
well outside the thermodynamic stability window of water. During recharge, water reduction (
) competes with zinc plating, causing parasitic gassing, loss
of Coulombic efficiency, and local pH shifts.
2. Practical Strategies for Reversible Zinc
Mild Aqueous Electrolytes (Sulfate/Acetate vs. Alkaline):
While commercial alkaline cells (using concentrated ) suffer from massive zinc
redistribution and dendrites due to highly soluble zincate , mildly acidic
Discharge: Zn  →(s) Zn  +(aq)
2+ 2e ⇌− Charge: Zn  +(aq)
2+ 2e →− Zn  
(s)
−0.76 V
2H  O +2 2e →− H  ↑2 +2OH−
KOH
[Zn(OH)  ]4
2−
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 31/92
or near-neutral electrolytes (such as  or ) drastically
improve cycle life.
In mild sulfate systems (pH ~4 to 5), zinc plates out far more smoothly and forms a self-
regulating interface.
High-Surface-Area Substrates (3D Current Collectors):
Instead of plating onto a flat zinc foil, using a 3D porous conductive host (such as
carbon paper, graphite felt, copper mesh, or porous brass) dramatically lowers the local
current density ( ).
Lower local current densities eliminate electric field hot-spots and promote compact,
planar nucleation rather than dendrite spikes.
Electrolyte Additives:
Small amounts of leveling agents or surface-active additives (e.g., trace polyethylene
glycol/PEG, trace , or sodium dodecyl sulfate) adsorb onto fast-growing dendrite
tips, forcing zinc to deposit uniformly into the valleys.
3. Pairing with Graphite Felt (The Zinc Deposition Chemistry)
When paired with a graphite felt cathode in an aqueous sulfate solution:
The Cathode Reaction: Often operates as a deposition/redox mechanism—for instance, in a
zinc manganese deposition battery, manganese ions in solution deposit onto the high-
surface-area graphite felt as  on charge ( )
and dissolve back into the electrolyte on discharge.
The Zinc Role: The zinc plate (or a 3D zinc-plated substrate) supplies  ions into the
bulk sulfate solution on discharge and plates metallic zinc back out during the constant-
current charge phase.
User prompt: What other chemistries were tested in trough battery in the 19th century? Lead acid
cells?
Response: The "trough" form factor evolved significantly throughout the 19th century as chemists
tried to overcome the rapid polarization and acid-corrosion problems of early cells. Multiple primary
and secondary chemistries were deployed in trough formats:
1. The Lead-Acid Trough (Secondary / Rechargeable)
Yes, lead-acid was built into troughs.
The Evolution from Planté to Faure (1860s–1880s): Gaston Planté originally made
rechargeable cells by rolling lead sheets into spirals separated by rubber strips in glass jars.
However, in the 1880s, when Camille Faure and the Electric Power Storage (E.P.S.)
Company scaled up commercial storage batteries using pasted grid plates, they moved to
1–2 M ZnSO  
4 Zn(CH  COO)  
3 2
mA/cm2
Mn2+
MnO2 Mn +2+ 2H  O →2 MnO  +2 4H ++ 2e−
Zn2+
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 32/92
multi-plate trough-style enclosures (often lead-lined wooden boxes or multi-compartment
vulcanized hard rubber troughs).
Why the Trough Suited Lead-Acid: The rigid rectangular trough geometry allowed heavy,
flat lead grids (  anode,  cathode in sulfuric acid) to be stacked compactly with
bottom sediment clearances ("mud ribs") to catch shedding oxide paste.
2. Multi-Cell Daniell Troughs (Telegraph Workhorses)
While Daniell cells were often individual ceramic pots, the British telegraph service adapted them
directly into standardized wooden troughs to power long lines:
The Muirhead Trough Battery (1857): A wooden trough divided into 5 or 10 compartments
by solid slate, porcelain, or gutta-percha partitions. Each compartment held a porous
earthenware pot separating copper in  from zinc in dilute sulfuric acid or water.
The Fuller Trough (Double-Fluid Trough): Similar multi-compartment trough using porous
flat tiles cemented into the frame rather than separate round pots.
3. The Poggendorff / Bichromate "Plunge" Trough (Zinc–Carbon)
Invented in the 1840s–1850s, this became the favorite high-current lab battery of the late 19th
century:
Chemistry: Zinc anode paired with hard carbon (retort carbon or graphite) in an aggressive
electrolyte of potassium bichromate ( ), sulfuric acid, and water (known as
electropoion fluid).
Trough Format: Built as a "plunge battery" where 6 to 12 pairs of zinc and carbon plates
were ganged to a single wooden beam above a multi-compartment porcelain or lead-lined
trough. Lowering the rack into the trough delivered massive, non-polarizing current at ~2.0 V
per cell; cranking the rack out of the trough stopped acid corrosion instantly when
experiments finished.
4. The Smee Trough (Zinc–Platinized Silver)
Invented in 1840 by Alfred Smee, this retained the simple single-fluid trough format but fixed
hydrogen polarization without needing toxic depolarizing liquids:
Chemistry: Zinc anode paired with a thin silver sheet coated in finely divided platinum
black in dilute sulfuric acid ( ).
Trough Design: Fitted directly into standard wooden troughs. The rough platinum black
dramatically lowered hydrogen overpotential, causing bubbles to detach continuously rather
than forming an insulating film. It was the premier power source for Victorian electrotyping and
silver electroplating.
5. Grove and Bunsen Two-Fluid Cells
Pb PbO  
2
CuSO
 
4
K  Cr  O  
2 2 7
1.0 V
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 33/92
Grove Cell (1839): Zinc in dilute acid paired with platinum foil in concentrated nitric acid (
) (~1.9 V).
Bunsen Cell (1841): Robert Bunsen replaced Grove's expensive platinum with cheap
compressed carbon blocks.
Trough Adaptations: While messy due to toxic nitrogen dioxide ( ) gas, series banks
were frequently arranged in long segmented troughs for arc-lighting and early electro-smelting
demonstrations.
Sources
1. History of the battery - Wikipedia
2. Daniell battery hi-res stock photography and images - Alamy
User prompt: The porous pots I can easily fine but they have drainage holes in them. What would
be a historically appropriate way to close those holes? I assume it doesn’t have to be porous.
Response: You are completely correct—the plug does not need to be porous. The separator's
job is simply to provide enough porous surface area for ion transport through its sidewalls; the floor
can be completely solid and impermeable.
Historically, 19th-century laboratory experimenters frequently had to adapt vessels, repair cracked
ceramics, or seal apparatus using the materials on hand.
Historically Authentic Sealing Methods
1. Rosin & Beeswax Battery Cement (The Best Historic Choice):
Melt standard electrical cement (5 parts rosin, 1 part beeswax, 1 part dried Plaster of
Paris).
Warm the clay pot base slightly so the cement doesn't freeze on contact.
Place a small backing disc (like a piece of thick card, parchment, or wood) on the
outside of the hole, then pour molten cement into the inside bottom of the pot to a depth
of 3–5 mm.
The hot resin wicks slightly into the open pores of the warm terracotta and sets into a
rigid, acid-proof, waterproof floor within minutes.
2. Gutta-Percha Plug (Mid-to-Late 19th Century Standard):
Natural latex from Palaquium gutta trees was the miracle thermoplastic of Victorian
telegraphy.
Heated in hot water until soft and pliable like clay, a wad of gutta-percha was jammed
into the drain hole and pressed flat on both sides. Once cold, it hardened into an
impermeable, highly acid-resistant rubber plug.
3. Natural Cork Sealed with Sealing Wax:
HNO  
3
NO  
2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 34/92
Taper and press a standard natural wine cork tightly into the hole.
Shave it flush with the pot interior, then paint or pool molten shellac sealing wax or pine
pitch over the cork and surrounding clay to seal the porous cork grain.
Modern Workshop Equivalents
If you want a fast, zero-fuss seal in the shop that behaves identically:
Plaster of Paris Plug: Mix a stiff dab of plaster, press it into the hole, and let it cure. While
the plaster itself remains slightly porous, it stops bulk liquid flow immediately.
100% Silicone Caulk or Rubber Grommet/Stopper: A dab of pure neutral/acid-cure silicone
pressed into the hole creates an inert seal that resists copper sulfate and dilute acid
indefinitely.
Hot Melt Glue: A thick drop of standard EVA hot glue over the hole provides a quick resinous
seal that mimics pitch or gutta-percha.
User prompt: What was the geometry of the electrodes and the outer jar?
Response: The classic 19th-century Daniell cell used a coaxial cylindrical geometry (concentric
cylinders nested inside one another). This radial symmetry kept the ionic path length identical in
every direction, minimizing internal resistance (  drop) and ensuring uniform current density.IR
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 35/92
The Two Historic Layouts
Layout A: The Original 1836 Metal-Can Design (Shown Above)
Outer Vessel (Cathode): A tall, narrow copper cylinder/can (typically 3.5" to 4"
diameter  6" to 8" tall). The vessel itself served as the copper cathode.
Crystal Shelf: A perforated copper annular ring or basket suspended just below the top
rim inside the outer chamber. Copper sulfate ( ) crystals sat on this shelf to
maintain solution saturation as copper plated out.
Porous Separator: A tall, unglazed terracotta/earthenware cylinder (1.5" to 2" diameter)
placed concentrically in the middle.
Center Core (Anode): A solid zinc rod or heavy-walled cast zinc cylinder (0.5" to 1"
diameter) suspended down the center axis inside the porous pot, immersed in dilute
acid or .
Layout B: The Glass Jar / Telegraph Design (Later 19th Century)
Outer Vessel: A heavy, wide-mouth glass or stoneware jar (often octagonal or round).
Outer Electrode (Cathode): A thin sheet of copper rolled into an open cylinder
lining the inside glass wall.
×
CuSO  
4
ZnSO  
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 36/92
Center: The unglazed porous pot was placed in the middle.
Inner Electrode (Anode): A cast zinc rod centered inside the pot.
Why Coaxial Cylinders Were Used
Equalized Current Density: A flat plate in a round jar causes current to crowd onto the
nearest edges, causing uneven zinc dissolution. Concentric cylinders ensure that every
square centimeter of the zinc anode faces the copper cathode at the exact same distance.
Compact Footprint: Nesting the components vertically delivered the maximum active
surface area within the smallest bench footprint.
Volume Distribution: The annular (outer) ring provided a large fluid reservoir for 
crystals and solution, while the smaller inner core kept the volume of required acid/zinc salt
minimal.
User prompt: Was the Daniel’s cell rechargable? I forget.
Response: In theory and chemical principle, yes—but in 19th-century practical use, no.
Historically, the Daniell cell was treated strictly as a primary (single-use / consumable) battery,
renewed mechanically by replacing the zinc rod and adding more blue vitriol ( ) crystals
rather than recharging it electrically.
The Theoretical Reversibility
Thermodynamically, the net Daniell cell reaction is fully reversible:
If you apply an external DC power source with a voltage greater than , copper will
dissolve back into solution at the cathode and metallic zinc will plate back onto the anode.
Why It Failed as a Practical Rechargeable Cell
Victorian experimenters attempting to electrically recharge Daniell cells ran into severe physical
failure modes:
Copper Ion Crossover & Self-Discharge: A porous earthenware pot or plaster separator
slows bulk liquid mixing, but it cannot stop continuous ionic diffusion. Over hours or days, blue
 ions slowly diffuse across the porous wall into the zinc chamber. The moment a 
ion touches the zinc anode, a spontaneous displacement reaction occurs:
CuSO  
4
CuSO
 
4
Discharge: Zn  +(s) Cu  ⟶(aq)
2+ Zn  +(aq)
2+ Cu  
(s)
Charge: Zn  +(aq)
2+ Cu  ⟶(s) Zn  +(s) Cu  
(aq)
2+
≈ 1.10 V
Cu2+ Cu2+
Cu +2+ Zn ⟶ Cu
 
+(s) Zn2+
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 37/92
This plates a spongy, black layer of metallic copper directly onto the zinc rod, creating
hundreds of short-circuited local micro-galvanic cells that rapidly corrode the zinc and kill the
cell via self-discharge even when idle.
Zinc Dendrites During Recharge: When forcing zinc to electroplate back onto the anode
during electrical charging, it deposits as fragile, mossy needles (dendrites) rather than a flat,
solid sheet. These dendritic spikes quickly grow across the separator pores, causing hard
internal short circuits.
Lack of DC Generators in 1836: When John Frederic Daniell invented the cell in 1836,
practical dynamos and electrical grids did not exist. There was no cheap, abundant source of
DC electricity to recharge secondary batteries, making mechanical replenishment (scraping
the zinc and dropping in fresh chemicals) the only viable operational workflow until Gaston
Planté introduced the lead-acid accumulator in 1859.
User prompt: How did 19th-century telegraph stations maintain, clean, and renew Daniell cells on a
routine schedule?
Response: Telegraph battery rooms housed hundreds to thousands of Daniell cells connected in
series strings, demanding a rigorous, quasi-industrial maintenance regimen by dedicated battery-
men ("battery attendants").
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 38/92
Daily & Weekly Routine Maintenance
Hydrometer Checks & Specific Gravity Management:
In two-fluid systems, the lighter zinc solution at the top would become overly dense as
zinc dissolved (  concentration rising).
Battery attendants checked specific gravity with a Baumé hydrometer. When the top
solution reached ~20°–25° Baumé, they used a battery syringe (a large rubber bulb
with a long glass tube) to siphon off the dense top liquid and replace it with fresh soft
water.
Topping Up Blue Vitriol ( ):
ZnSO  
4
CuSO
 
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 39/92
Attendants regularly dropped fresh crystals of copper sulfate down chutes or directly
onto the crystal shelf.
The rule of thumb was to keep the crystal bed submerged to ensure the bottom cathode
electrolyte remained fully saturated.
Creeping Salt Mitigation:
Sulfate salts constantly wicked up the porous pot walls and jar rims via capillary action,
forming white crusty blooms that created surface leakage paths to ground.
Rims were periodically swabbed with warm water, and the top 1–2 inches of jars were
painted with paraffin wax, mineral oil, or lard to stop the salt creep.
Monthly / Quarterly Deep Cleaning ("The Battery Overhaul")
Every 1 to 3 months, entire battery banks were taken offline in rotation for complete mechanical
teardown:
1. Scraping the Zinc Anodes:
Attendants pulled the zinc rods/crowfeet, which were heavily caked in black, spongy
copper mud (from unavoidable copper-ion crossover) and zinc oxide sludge.
Zincs were wire-brushed, scraped down to bare metal with draw-knives, and weighed.
Severely thinned zincs were melted down in a shop crucible and recast into new rods.
2. Re-Amalgamating with Mercury:
After scraping, zincs were dipped in dilute sulfuric acid and rubbed with liquid mercury
using a stiff rag until a bright, reflective liquid-metal mirror formed. This suppressed local
iron-impurity galvanic action ("local action").
3. Porous Pot Leaching:
Terracotta pots were soaked in large tubs of boiling water and weak acid for days to
dissolve crystallized copper and sulfate plugs out of the ceramic pores, restoring ion
permeability.
4. Copper Reclamation:
The solid metallic copper that had plated out of solution onto the cathodes was peeled
off in sheets and sold back to scrap dealers or reused in foundry melts.
Trough vs. Gravity Cell Operational Differences
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 40/92
Factor
Porous Pot Trough
(Muirhead / Standard
Daniell)
Gravity "Crowfoot" Cell (Late 19th Century)
Separation
Method
Rigid unglazed clay pot
or cast divider
Fluid density alone (dense blue  on
bottom, clear light  on top)
Maintenance
Burden
High; pots clogged with
crystals and cracked if
left dry.
Lower; zero pots to scrub or break.
Requirement Could tolerate slight
bench vibrations.
Had to remain completely undisturbed on shock-
isolated wooden racks; vibration mixed the
density boundary.
Closed-Circuit
Need
Could sit on open circuit
without rapid mixing.
Required continuous light current draw (closed
loop) to keep the blue copper line driven down
away from the zinc crowfoot.
User prompt: Ah, the shelf increased the capacity of the cell by restocking the copper sulfate. Was
the sulfuric acid next to the zinc needing replenishment?
Response: No, the acid didn't run out—in fact, the opposite happened: the zinc chamber
became choked with excess zinc salt and needed to be diluted.
What Actually Happened at the Zinc Anode
When the cell discharged, zinc oxidized into solution:
If started with dilute sulfuric acid ( ): The acid naturally converted into zinc sulfate (
). As discharge continued, the liquid around the zinc grew progressively denser and
more concentrated with  and  ions.
The Problem of Oversaturation: Once the zinc solution became near-saturated, several
issues arose:
1. Voltage Sag: As  concentration spikes, the Nernst equation shows cell voltage
drops (from  down toward ).
2. Internal Resistance Spike: Extremely concentrated zinc sulfate increases the internal
resistance of the liquid.
3. Crystallization: White  crystals would begin crusting over the zinc anode and
clogging the microscopic pores of the earthenware pot.
CuSO  
4
ZnSO  
4
Zn  ⟶(s) Zn  +(aq)
2+ 2e−
H  SO  
2 4
ZnSO
 
4
Zn2+ SO  
4
2−
[Zn ]2+
≈ 1.14 V ≈ 1.05–1.08 V
ZnSO  
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 41/92
How Attendants Handled It: Dilution, Not Addition
Instead of adding acid or salt, the standard operational protocol was to siphon out concentrated
zinc liquid and add plain water:
1. The attendant used a rubber battery syringe to draw off the dense, heavy  liquid
sitting around the zinc.
2. They refilled the compartment with fresh soft water.
3. The remaining dissolved salts and migrating sulfate ions were more than enough to maintain
electrical conductivity without adding any new acid.
The Telegraph Transition: Abandoning Acid Entirely
In early laboratory Daniell cells, dilute sulfuric acid was initially used around the zinc to lower
internal resistance. However, acid caused local parasitic corrosion (the acid slowly ate the zinc
metal even when the telegraph line was idle).
By the 1850s, telegraph networks largely abandoned acid in the porous pot:
They filled the zinc chamber with plain water (or a very weak, dilute pinch of  or
 just to start initial conduction).
As soon as current was drawn, the zinc dissolved, generating its own  electrolyte in
situ.
This eliminated parasitic acid bubbling, extended zinc life dramatically, and simplified
maintenance to two simple rules: keep the copper side supplied with blue crystals, and
periodically dilute the zinc side with water.
Sources
1. Daniell
2. Daniell Cell | Youblob
User prompt: I’m not sure I understand how the Daniel cells were integrated into the wooden
troughs
Response: In a Cruickshank trough, the bimetallic plates are the physical dividers. But a Daniell
cell requires two different electrolytes (  and /water) separated by a porous barrier.
To make this work in a long wooden trough, 19th-century telegraph engineers abandoned the
bipolar metal divider and used solid, liquid-tight insulating partitions, organizing the trough in
one of two ways:
1. The Muirhead Trough Design (Most Common)
This was the standard British Post Office and telegraph trough:
ZnSO  
4
ZnSO  
4
MgSO4
ZnSO  
4
CuSO  
4 ZnSO  
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 42/92
Solid Cell Compartments: A long wooden box (usually teak or mahogany lined with pitch)
was divided into 5 or 10 completely watertight compartments using solid partitions of slate,
porcelain, or gutta-percha.
Porous Pot Inside Each Cell: Inside each watertight compartment sat a flat, rectangular
unglazed earthenware porous pot.
Liquid Separation:
Outer chamber (around the pot): Filled with saturated copper sulfate ( )
solution, blue vitriol crystals, and a flat sheet of copper.
Inner pot: Filled with water / dilute zinc sulfate and a zinc plate.
Jumper Across the Partition: A thick copper strap or wire was soldered to the copper plate
in Cell 1, arched over the solid partition wall, and connected to the zinc plate in Cell 2.
       [--- SOLID PARTITION ---]       [--- SOLID PARTITION ---]
       |                       |       |                       |
       |  +-----------------+  |       |  +-----------------+  |
       |  |   POROUS POT    |  |       |  |   POROUS POT    |  |
       |  |  (Zinc + Water) |  |       |  |  (Zinc + Water) |  |
       |  +-----------------+  |       |  +-----------------+  |
       |                       |       |                       |
       |   Copper + CuSO4      | =====>|   Copper + CuSO4      |
       |   (Outer Chamber)     | Strap |   (Outer Chamber)     |
       +-----------------------+       +-----------------------+
                CELL 1                          CELL 2
2. The Fuller Trough Design (The Sub-Divided Trough)
In this variant, the trough had two layers of dividers:
Alternating Dividers: The trough used alternating solid slate dividers (to isolate cells
electrically) and unglazed porous earthenware tiles (to act as the ionic diaphragm between
the two halves of a single cell).
Two Halves per Cell: Each cell had a dry slate wall on the left and right, and a porous clay
plate cemented down the middle.
Side A: Zinc plate in water/acid.
Side B: Copper plate in .
Top Connection: As before, the electrical connection was an external metal bridge hopping
over the solid slate barrier into the next compartment.
Why the Trough Format Won Out for Telegraphy
While individual round glass or copper jars were used in small laboratories, telegraph relay stations
needed 50 to 100+ cells in series. Putting 10 cells in a single 24-inch wooden trough gave
CuSO  
4
CuSO
 
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 43/92
operators:
1. A compact, stackable footprint that fit onto multi-tier battery racks.
2. Reduced wire clutter, since adjacent cells were linked by short rigid straps right over the
partition rim.
3. Spill containment, with the outer wooden trough coated in bitumen/pitch to prevent leaks.
Sources
1. Electrical telegraphy in the United Kingdom - Wikipedia
User prompt: Is the copper sheet in the copper sulfate just a current collector? Or is it involved
chemically
Response: It is actively involved in the electrochemistry as the deposition substrate, not just
an inert current collector.
In a Daniell cell, the copper sheet serves as both the electrical lead and the physical destination
where copper ions plate out into new solid metal.
What Actually Happens at the Copper Electrode
During discharge, electrons arrive at the copper cathode from the external circuit. Dissolved
copper(II) ions in the electrolyte absorb those electrons directly at the metal surface:
Mass Gain: Fresh metallic copper constantly plates onto the sheet. As the cell runs, the
copper plate grows thicker and heavier.
Potential Definition: The chemical identity of the metal and ion pair ( ) directly
establishes the standard reduction potential of the cathode half-cell (+0.34 V vs. SHE).
Could You Use an Inert Material Instead?
Graphite or Carbon: If you replaced the copper sheet with a graphite plate or carbon rod, the
cell would still work at the same potential (~1.1 V). The  ions in the  solution
would simply electroplate a thin layer of copper directly onto the carbon surface within
seconds of closing the circuit, effectively turning it into a copper electrode in situ.
Why Copper Sheet Was Used: Starting with clean copper provides zero nucleation
overpotential, excellent electrical conductivity, and prevents the flaking or adhesion issues
that happen when copper plates onto inert graphite over long discharge periods.
Cu  +(aq)
2+ 2e ⟶− Cu
 
(E =(s)
∘ +0.342 V)
Cu /Cu2+ 0
Cu2+ CuSO  
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 44/92
User prompt: The muirhead design was connected from the zinc rod to the copper sheet in the next
cell. The fuller design would be a simple strap from the zinc side to the copper side.
Response: Exactly.
In both designs, the jumper bridges across the solid insulating partition to put the cells in series:
Muirhead Layout: A long jumper wire or formed strap extends from the center zinc rod
inside the nested porous cup, arches up and out of the pot, crosses the solid cell bulkhead,
and connects to the large copper sheet lining the outer chamber of the adjacent cell.
Fuller Layout: Because the porous tile divides the compartment into two side-by-side halves,
the plates sit right next to the outer walls. A short, rigid metal "U-strap" or saddle clamp simply
hops over the top edge of the solid slate divider—clamping the zinc plate in Cell 1 to the
copper plate in Cell 2.
--- FULLER SUB-DIVIDED TROUGH (TOP VIEW) ---
    [============ SOLID SLATE DIVIDER ============]
    |                                             |
    |      CELL 1 (Left)        CELL 1 (Right)    |
    |      Zn in water          Cu in CuSO4       |
    |                                             |
    |  [ Zn Plate ]             [ Cu Plate ]      |
    |       |                        |            |
    |  .....|... POROUS TILE ........|..........  |
    |       |                        |            |
    |       |                        |            |
    [=======|==== SOLID SLATE DIVIDER|============]
            |                        |
            |     === U-STRAP ===    |  <-- Series Jumper
            +------------------------+
            |                        |
    |  [ Zn Plate ]             [ Cu Plate ]      |
    |                                             |
    |      CELL 2 (Left)        CELL 2 (Right)    |
    |      Zn in water          Cu in CuSO4       |
    |                                             |
    [============ SOLID SLATE DIVIDER ============]
Why the Fuller Design Was Popular in Shops
The Fuller setup mirrored the look and feel of the original Cruickshank layout, but with the critical
operational upgrade:
1. Zero through-hole leaks: The solid bulkheads remained unbroken and completely sealed
with pitch/cement.
2. Simplified plate replacement: When a zinc plate dissolved or fouled, an attendant could
unclip the top U-strap and slide the old zinc out of its slot without disturbing the cement seal
or draining the adjacent copper chamber.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 45/92
User prompt: The cruickshank layout didn’t have holes in the bulkheads? Or do you mean leaks
around the edges of the bipolar plates? Wouldn’t that also be a problem sealing the slate or
ceramic?
Response: Yes, exactly—the leaks were around the perimeter edges where the plates met the
wooden groove, not through holes in the metal.
In Cruickshank's original design, the metal plates themselves were the bulkheads.
Why Sealing Slate/Ceramic in Pitch Was Far More Reliable
Sealing a non-metal partition (slate, glazed porcelain, earthenware tile) with rosin/pitch cement
proved dramatically more dependable over time than sealing a metal plate, due to three physical
mechanisms:
1. Thermal Expansion Matching:
Pine Rosin / Pitch: Thermal expansion coefficient .
Slate / Terracotta Tile: .
Wood (along/across grain): .
Zinc & Copper: . More importantly, as copper and zinc
conducted heat from chemical reactions or current, the metal expanded and contracted
rapidly. The slick, non-porous metal faces sheared away from the rigid resin cement,
forming hairline boundary cracks that leaked electrolyte across cells.
2. Porous Mechanical Keying:
Ground slate, rough unglazed porcelain edges, and terracotta tiles have microscopic
surface porosity and tooth.
Hot molten rosin and pitch wick directly into the ceramic surface grain before solidifying,
creating a deep, locked mechanical anchor. Pitch bonds tenaciously to stone and wood,
whereas its bond to smooth, oxidized zinc or copper sheet is prone to delamination.
3. Galvanic Creep & Chemical Undermining at the Seal Edge:
In a Cruickshank trough, active battery acid sat right against the joint where the zinc met
the resin. As the zinc dissolved during discharge, the metal surface under the cement
physically receded, undermining the joint.
In a slate-divided trough, the slate partition is completely inert—acid and salts cannot
dissolve it, so the cement-to-slate interface remains undisturbed indefinitely.
By separating the hydraulic partition wall (inert slate/tile permanently sealed in pitch) from the
replaceable electrodes (slid in loosely and connected over the top rim), telegraph engineers
solved the constant weeping and inter-cell short circuits that plagued Cruickshank troughs.
α ≈ 60–80 × 10  /K−6
α ≈ 8–12 × 10  /K−6
α ≈ 5–30 × 10  /K−6
α ≈ 17–30 × 10  /K−6
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 46/92
User prompt: I can find 4” ceramic and slate tiles, that would make the replica a bit smaller. I could
cast larger plaster of Paris separators. Slate is harder, unless it is possible to cut pieces out of slate
cheeseboards 8”x12”
Response: Yes, slate cheeseboards cut surprisingly easily—they are actually one of the
cheapest and most authentic sources of genuine raw slate for workshop projects.
Because slate is a fine-grained, foliated metamorphic rock (essentially compressed clay and silt), it
has a Mohs hardness of only 2.5 to 4.0. It behaves much softer than granite or vitreous porcelain,
but it is brittle and prone to delaminating along its natural cleavage planes if forced.
How to Cut Slate Cheeseboards Cleanly
Best Method: Diamond Wheel on an Angle Grinder (or Wet Tile Saw)
A standard continuous-rim or fine-serrated diamond masonry blade (4" or 4.5") on an
angle grinder cuts 5–8 mm thick cheeseboard slate in under 30 seconds.
Clamp a rigid straight-edge (scrap wood or steel ruler) to the slate as a guide.
Cut all the way through in 2–3 light passes rather than scoring and snapping.
Snapping along a score line can cause the internal natural grain to split diagonally
across layers.
Alternative: Carbide/Diamond Grit Jigsaw Blade or Hacksaw
A fine grit jigsaw blade run at slow speed without orbital action will cut straight lines
through cheeseboard slate.
Dust & Safety:
Slate dust contains crystalline silica. Cut outdoors and use a continuous fine
spray/dribble of water from a squirt bottle to keep dust suppressed and blade temps
cool.
Edge Dressing:
Once cut, the edges can be trued up or deburred in seconds with 80-grit to 120-grit wet
sandpaper on a flat block.
Casting Plaster of Paris Separators
For the unglazed porous partitions, casting your own Plaster of Paris (hemihydrate gypsum) tiles
is straightforward and historically sound (gypsum diaphragms were standard DIY substitutes in
19th-century chemistry labs):
Thickness: Aim for 4 mm to 6 mm (~3/16" to 1/4"). Any thinner and they become fragile
when wet; much thicker and internal ionic resistance rises.
Mix Ratio: Mix standard plaster slightly "wet" (approx. 100 g plaster to 70–75 g water) to
increase the open capillary porosity of the cured gypsum crystal matrix without compromising
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 47/92
structural handling.
Release Mold: Pour into an open silicone baking mold, a 3D-printed form lined with
parchment/PET tape, or Lego bricks on a smooth sheet.
Curing & Pre-wetting: Let cure for 24 hours. Always pre-soak the dry plaster tiles in
clean water or dilute electrolyte before seating and running the cell so air bubbles inside
the micro-pores are fully displaced.
Sources
1. Tips on Cutting and Preparing Slate - Second Use Building Materials
2. Working with Slate - Lenco Heaven
User prompt: I think I’d make a 3dp printed mold for a silicone mold for the plaster. What kind of
current was needed to run a telegraph line ?
Response: Typical telegraph lines operated on surprisingly tiny currents: roughly 15 to 50
milliamperes (0.015 to 0.050 A).
Because the iron telegraph wire stretched for tens or hundreds of miles, lines were high-resistance,
voltage-limited circuits rather than high-current systems.
Standard Operating Currents by Equipment Type
Instrument / System Operating
Current Why This Range Was Chosen
Sensitive Polarized Relays
(Long-distance trunk lines) 15 to 25 mA High-turn electromagnets could trip a sensitive,
counterbalanced armature on minimal current.
Standard Morse Registers &
Sounders (Local loops / Main
lines)
30 to 50 mA
Needed enough magnetic force to make a crisp,
loud physical "click" on brass stops without an
intermediate relay.
Needle Telegraphs (British
Railways / Cooke &
Wheatstone)
10 to 25 mA Moving a lightweight magnetic needle over a
dial required barely any power.
Why Voltage, Not Current, Dictated Battery Size
A 100-mile single iron wire line (plus ground return, key, and electromagnet coil resistance) easily
totaled  of circuit loop resistance.
By Ohm's Law ( ):
To push just  ( ) through a  line:
1, 500 to 3, 000 Ω
I = V /R
30 mA 0.030 A 2, 000 Ω
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 48/92
Since a single Daniell cell delivers , telegraph stations had to string 50 to 60 Daniell
cells in series (often five or six 10-cell wooden troughs ganged together) just to overcome
the line resistance.
Because each cell only needed to deliver , small 3" or 4" plates operated at a very
comfortable current density ( ). This kept polarization negligible and allowed a
battery bank to run reliably for weeks before needing water dilution or a top-up of blue crystals.
User prompt: So the key was used to send and the sounder was the receiver?
Response: Yes, exactly—the telegraph key was the momentary switch used to transmit, and
the sounder was the acoustic receiver.
Every station along the line had both a key and a sounder wired in series with the battery and the
single overhead iron line wire (using the earth as the return path).
How the Two Instruments Worked Together
The Key (Transmitter):
A spring-loaded, single-pole momentary switch.
Tapping the knob brought an upper contact down onto an insulated lower anvil, closing
the electrical loop and sending current down the line for the duration of the tap (short for
dots, longer for dashes).
The "Circuit Closer" Switch: Notice the small black lever on the left of the key above.
American Morse systems ran on a normally closed loop. When an operator finished
sending, they closed this lever to complete the circuit for other stations. When ready to
send, they opened the lever, taking control of the line.
The Sounder (Receiver):
An electromagnet with a spring-loaded iron armature attached to a heavy brass
crossbar.
When current flowed through the coils, the electromagnet pulled the armature down
against an adjustable brass anvil with a sharp "click" (down-stroke).
When current stopped, a return spring yanked the crossbar up against an upper stop
screw with a slightly different "clack" (up-stroke).
Operators didn't listen to continuous tones—they read Morse code purely by the rhythm
and time interval between the down-click and the up-clack.
Long-Distance Lines: Adding the Relay
V = I × R = 0.030 A × 2000 Ω = 60 Volts
≈ 1.1 V
∼ 30 mA
< 0.5 mA/cm2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 49/92
On long lines (50–200+ miles), line resistance weakened the signal down to ~15–20 mA—too weak
to pull a heavy sounder crossbar with a loud click.
Telegraphers placed a sensitive Relay on the main line:
1. The weak line current tripped the featherweight armature of the relay.
2. The relay contacts acted as an automated key for a separate, private "Local Circuit" in the
office.
3. A small local 1- or 2-cell Daniell battery then powered the loud, heavy sounder directly at full
current (50–100 mA).
User prompt: Were there repeater stations automatically amplifying the signal
Response: Yes, automatic telegraph repeaters were invented in the 1850s and 1860s
specifically to solve the distance limit without human re-transcription.
Before repeaters, a telegraph operator at an intermediate station (every 150–250 miles) had to
listen to the incoming Morse sounder with one hand and manually re-tap the message onto the next
line with their own key.
The Engineering Dilemma: The Feedback Loop
Building an automatic repeater was not as simple as wiring Relay 1 directly into Line 2:
If Line East activates Relay East, which keys Line West...
The moment Line West activates, it trips Relay West, which immediately keys Line East
right back.
This creates a permanent electromechanical feedback loop (called "lock-up" or "chatter").
Because telegraph lines were bidirectional (either station could send or interrupt), an automatic
repeater had to detect which direction the message was traveling and instantly lock out the reverse
path.
How 19th-Century Automatic Repeaters Worked
Inventors like George F. Milliken, Thomas Edison, and Moses G. Farmer developed ingenious
interlocking electromechanical circuits (such as the Milliken Repeater and Weiny-Phillips Repeater):
Dual Main Line Relays: The station had two separate line circuits—one going East, one
going West—each with its own large battery bank.
Mechanical / Auxiliary Lockout Relays: When Line East pulsed, Relay East tripped an
intermediate local transmitter. As this transmitter closed the circuit for Line West, it
simultaneously energized a holding coil or dropped a mechanical latch onto Relay West.
Breaking the Feedback: This physical lockout prevented Relay West’s contacts from
opening when Line West opened, stopping the feedback loop while faithfully repeating the
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 50/92
pulses forward at full line voltage.
What It Achieved
By placing automatic repeaters in junction towns every 200 to 300 miles, networks like Western
Union could link New York to San Francisco (over 3,000 miles) in a single instantaneous circuit.
When an operator in New York tapped their brass key, a cascade of 10 to 15 automatic repeaters
across the continent opened and closed in microsecond synchronization, keying fresh
Daniell/gravity battery banks down each succeeding leg of wire.
Sources
1. Thomas Alva Edison | Encyclopedia.com
User prompt: How do I wire a two-station Morse telegraph circuit with keys, sounders, and
batteries?
Response: The standard American system used a closed-circuit loop: every key, sounder, and
battery along the line was wired in one continuous series circle.
The Series Wiring Schematic
On a bench or between two rooms, wire the components in a single continuous loop (using a return
wire instead of an earth ground rod):
+------------------ [ LINE WIRE ] --------------------+
|                                                     |
|                  STATION A                          |
|   +----[ Sounder A ]----+                           |
|   |                     |                           |
|   |   +-[ Key A ]-+     |                           |
|   |   |  (Sw A)   |     |                           |
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 51/92
|   |   +-----------+     |                           |
|   |         |           |                           |
| [Battery A] |           |                           |
|   |         |           |                           |
+---+---------+           |                           |
                          |                           |
                          |                  STATION B|
                          |   +----[ Sounder B ]----+ |
                          |   |                     | |
                          |   |   +-[ Key B ]-+     | |
                          |   |   |  (Sw B)   |     | |
                          |   |   +-----------+     | |
                          |   |         |           | |
                          |   |         |           | |
                          |   +---------+-----------+-+
                          |             |
+-------------------------+-------------+
Station A:
1. Battery positive  connects to Line Wire running to Station B.
2. Battery negative  connects to one terminal of Key A.
3. The other terminal of Key A connects to Sounder A.
4. The second terminal of Sounder A connects to the Return Wire.
Station B:
1. The Line Wire connects to Sounder B.
2. The other terminal of Sounder B connects to Key B.
3. The other terminal of Key B connects back to the Return Wire. (Note: A single battery
bank at Station A can power the entire small loop, or you can split cells between Station
A and Station B, ensuring all batteries face the same series direction:  to ).
How to Operate the Circuit (The "Circuit Closer" Routine)
1. Idle State (Closed Loop):
Both operators keep the small side lever (circuit closer) on their keys closed.
Current flows continuously through the entire loop ( ).
Both sounders remain energized and pulled down in the quiet "clack" position.
2. Taking the Line to Transmit:
Station A flips open their side lever.
(+)
(−)
+ −
≈ 30–50 mA
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 52/92
The circuit opens: current drops to zero, and both sounders pop up.
3. Sending Morse:
Station A taps the key knob.
Every tap completes the circuit, pulling both Sounder A and Sounder B down
simultaneously with a loud "click."
Station A hears their own transmission (local sidetone), while Station B reads the
message.
4. Restoring the Line:
Once finished, Station A flips their side lever shut.
Current resumes, keeping the line closed and ready for Station B to open their lever and
reply.
User prompt: So just a sounder and a key wired to the battery would be enough to simulate the
sending side of the loop.
Response: Yes, exactly—wiring a single key, sounder, and battery in series gives you a
complete, authentic "local practice set."
Historically, telegraph companies sold this exact setup as a standalone learner's set mounted on a
single walnut board for trainee operators to practice keying and reading Morse code.
       +---[ Battery ]---+
       |   (1–3 Cells)   |
       |                 |
       |                 |
   [ Key ]-----------[ Sounder ]
How to Hook It Up on the Bench
1. The Circuit:
Wire the  terminal of your battery trough to one post of the Key.
Wire the other post of the Key to one coil terminal of the Sounder.
Wire the second coil terminal of the Sounder back to the  terminal of the battery.
2. Key Setup:
Leave the key's side switch (circuit closer) open so current only flows when you press
the knob.
(+)
(−)
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 53/92
Every time you tap a dot or dash, the circuit completes, energizing the electromagnet to
slam the armature down against the brass anvil with a crisp "click"; releasing it lets the
spring yank the crossbar up with a "clack."
Voltage & Battery Sizing for a Local Set
Because there are no miles of high-resistance line wire on a workbench, you only need to
overcome the internal resistance of the sounder coil itself:
For a Low-Resistance Sounder (4  – "Local Sounder"):
Needs roughly  for a loud strike.
 ( ) is plenty.
For a High-Resistance Mainline Sounder (20  to 150 ):
Needs roughly .
 ( ) provides enough drive voltage.
User prompt: Why were the troughs in England made of mahogany or teak? Wouldn’t oak have
been cheaper? Were these mitered boxes or some other joinery?
Response: Why Mahogany and Teak Beat Oak
While English oak was locally available, it had fatal chemical and physical flaws for battery
enclosures:
Tannic Acid Attack: Oak contains very high concentrations of natural tannic acid. When
exposed to warm, humid environments or sulfuric acid vapors, the tannins leach out, corrode
nearby metals, and chemically degrade the adhesion of rosin/pitch electrical cements.
Dimensional Instability (Warping & Movement): Oak expands and shrinks dramatically
across its grain with changes in relative humidity. A trough holding wet electrolytes would
swell on the inside and dry on the outside, breaking the brittle rosin/pitch seals around the
divider slots and causing cross-cell leaks.
Why Mahogany: Honduran/Cuban mahogany has exceptionally low volumetric shrinkage,
straight interlocking grain that resists cupping, and virtually no reactive tannins. It was the
standard for Victorian scientific instrument cases.
Why Teak: Teak (imported widely via the Royal Navy and British East India trade) is naturally
saturated with silica and hydrophobic natural tectoquinones/oils. It is virtually rot-proof,
completely impervious to acid vapors, and will not warp even under direct, continuous
moisture.
Historic Joinery Methods
Ω
100 to 250 mA
1 to 2 Daniell cells ≈ 1.1 to 2.2 V
Ω Ω
30 to 50 mA
2 to 4 Daniell cells ≈ 2.2 to 4.4 V
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 54/92
Simple miter joints were never used because end-grain glue bonds cannot resist the hydraulic
pressure of fluid or the mechanical stress of swelling partitions. Instrument makers used heavy,
interlocking mechanical joints:
Through Dovetails or Half-Blind Dovetails (The Standard):
The four outer walls of high-end lab troughs and Post Office telegraph boxes were
joined with fine hand-cut through dovetails.
Dovetails provided immense tensile strength at the corners, preventing the long side
walls from bowing outward under the weight of the plates and acid.
Rabbet (Rebate) & Box Joints (Utility Telegraph Troughs):
Mass-produced railroad troughs often used pinned rabbet joints or machine-cut
finger/box joints, frequently reinforced with brass or copper pins (iron screws/nails
corroded instantly in acid fumes).
The Bottom Floor Joint:
The bottom board was not simply nailed to the bottom rim. It was seated into a
continuous plowed groove (dado/rebate) cut around the inner base of the four walls,
then completely flooded and potted with molten pitch/rosin to create a seamless, liquid-
tight basin.
User prompt: What would the bottom of the trough be made of, I assume they didn’t have plywood?
Response: It was made of a single thick, solid hardwood board (usually quarter-sawn).
Modern cross-laminated waterproof plywood did not exist in the 19th century. Instead, instrument
makers and telegraph workshops used solid timber slabs with specific woodworking techniques to
manage moisture and hydraulic pressure.
How 19th-Century Makers Built the Bottom
Solid Slab Construction:
The bottom was a single piece of 0.75" to 1.0" (19 mm to 25 mm) thick solid
mahogany, teak, or well-seasoned pitch pine.
If a wide trough exceeded the width of a single available board, pieces were joined with
rubbed hide-glue joints reinforced with internal splines or tongue-and-groove
milling, but narrow single boards (4" to 6" wide) were preferred to eliminate seams
entirely.
Quarter-Sawn Grain Selection:
Makers deliberately chose quarter-sawn stock (growth rings perpendicular to the face).
Quarter-sawn boards expand and contract primarily in thickness rather than width, and
they do not cup or bow when wet on one side and dry on the other.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 55/92
How It Was Joined to the Sides:
Captured Bottom Groove (Dado): The bottom board was captured in a 1/4" to 3/8"
deep rebate/dado plowed along the inner perimeter of the four side walls before the
dovetail corners were assembled.
Floated & Bedded: The board was cut slightly shy of the groove bottom to allow for
minor cross-grain swelling, and the entire groove was flooded with hot pine pitch/rosin
cement during assembly rather than rigid glue.
The Interior Waterproof "Basin"
Because no raw solid wood floor could stay completely watertight against standing acid and copper
sulfate solutions indefinitely, the wooden box acted purely as a structural exoskeleton:
1. Hot Pitch Flooding: Once the box was assembled and dovetails pinned, boiling-hot pine
pitch, bitumen, or rosin/wax cement was poured into the bottom to a depth of 1/4" to 1/2" (6
mm to 12 mm).
2. Seamless Pan: This created a monolithic, seamless, chemical-proof resin "pan" across the
floor that permanently sealed the joints between the bottom board and side walls.
3. Groove Seating: The vertical divider kerfs (slots) cut into the walls terminated right into this
pitch bed, ensuring no liquid could track underneath the partitions.
User prompt: Rebate or dado is a groove or right on the bottom edge.
Response: A dado is an enclosed channel spaced in from the edge, while a rebate (rabbet) is
an open step cut right on the edge.
In traditional box making and trough construction, the distinction determines whether the bottom
board is fully captured or recessed into the perimeter rim.
The Two Joint Profiles
Rebate / Rabbet (Step on the edge):
Cut right along the corner/edge of the board (has one wall and an open shoulder).
In trough building, running a rebate around the bottom inside rim lets the floor board
drop in from above (or push up from underneath), sitting flush with the bottom edge.
       REBATE (RABBET)
       |   |
       |   |  <-- Side Wall
       |   +-------+
       |           |  <-- Step cut right on the corner
       +-----------+
Groove / Dado (Enclosed channel):
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 56/92
Spaced up from the edge (has two parallel walls and an enclosed floor).
Technically: a groove runs with the grain; a dado (or housing) runs across the grain.
In trough construction, running a groove about 1/4" to 3/8" above the bottom edge lets
the floor board slide in and get fully captured on all four sides like a drawer bottom
before the final dovetail or corner joint is closed.
       CAPTURED GROOVE
       |   |
       |   |  <-- Side Wall
       |   +---+
       |       |  <-- Groove spaced in from the bottom
       |   +---+
       |   |
       +---+  <-- Bottom rim
Which Was Used for Troughs?
Captured Groove (Most Common for Quality Troughs):
Machining a 1/4" wide groove spaced 3/8" up from the bottom edge locks the hardwood
floor mechanically into the side walls. Even under hydraulic weight, the bottom cannot
drop out or sag.
Bottom Edge Rebate (Utility Telegraph Troughs):
A 3/8" deep rebate cut around the bottom inner perimeter allowed the floor to be
dropped into the assembled frame, pinned horizontally with brass dowels, and then
flooded with molten rosin/pitch to seal the corner seam.
User prompt: 19 mm is pretty thick?
Response: Yes, 19 mm (~3/4") is beefy for a small box, but it was necessary to withstand the
physical demands of 19th-century battery use.
For a standard jewelry or tool box, 19 mm would be overkill. For a wet battery trough, that thickness
solved three structural and operational issues:
Why 19 mm Was the Historic Standard
1. Heavy Dado Depth vs. Remaining Wall Strength:
To hold 10 to 50 heavy divider plates upright against fluid movement, builders cut
vertical kerfs/dados 3 mm to 5 mm (1/8" to 3/16") deep into the inner sidewalls.
In a thin 10 mm (~3/8") board, a 4 mm groove would remove almost half the wall
thickness across 20+ vertical lines, effectively turning the sides into flexible, perforated
scoreboards prone to snapping.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 57/92
In a 19 mm wall, a 4 mm groove leaves 15 mm (~5/8") of solid hardwood behind the
slot, keeping the long box rigid and straight.
2. Preventing Cross-Grain Cupping & Bowing:
The inside of the trough was constantly saturated with wet electrolyte, while the outside
was exposed to dry air.
This extreme humidity differential creates severe asymmetric expansion that causes thin
boards to curl and cup outward. A 19 mm quarter-sawn board provides the mechanical
stiffness needed to resist bowing, keeping the cement seals around the plates intact.
3. Fluid Mass and Handling:
A full 10-cell trough loaded with slate partitions, zinc plates, copper sheets, crystals, and
liquid easily weighed 15 to 25 lbs (7 to 11 kg).
The trough had to be carried by its ends or rim during maintenance without flexing; flex
would instantly shatter the brittle rosin/pitch cement seams and cause inter-cell cross-
leaks.
Modern Scale-Down for a DIY Bench Model
For a smaller 5- to 10-cell decorative or experimental bench replica using 3" or 4" plates:
Part Historic Standard Practical Modern DIY
Side & End Walls 19 mm to 25 mm (3/4" to 1") 12 mm to 15 mm (1/2" to 5/8")
Bottom Board 19 mm (3/4") 12 mm (1/2") solid hardwood
Kerf / Groove Depth 4 mm to 5 mm 2.5 mm to 3 mm (approx. blade kerf)
Dropping down to 12 mm (~1/2") keeps the box lighter and more proportioned for a small desk set
while still leaving 9 mm of meat behind standard saw-blade kerfs.
User prompt: I’m thinking I need to practice with some cheaper wood first. Any suggestions for
similar machinjing characteristics but cheaper? Maybe without the good movement and moisture
characteristics
Response: Here are the best practice woods that mimic genuine mahogany’s crisp machining and
chisel behavior without the high price tag:
Top Practice Species
1. Yellow Poplar (Liriodendron tulipifera) — The Best Budget Stand-In
Cost: Very cheap; widely available at local home centers and hardwood yards.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 58/92
Machining Behavior: Machines smoothly without dulling blades, takes clean table-saw
dados, and routes cleanly with minimal burning.
How it compares: It is slightly softer than mahogany (Janka hardness ~540 vs. ~800–
900), which means hand chisels cut through it with less resistance, but end-grain can
get slightly "fuzzy" if tools aren't razor sharp. It moves significantly with moisture
changes, making it ideal purely for sizing, setup, and joint trials.
2. Sapele or African Mahogany (Khaya) — The Closest Direct Match
Cost: Roughly 40–50% cheaper than genuine Honduran mahogany (Swietenia
macrophylla).
Machining Behavior: Shares mahogany's medium-dense feel under chisels and router
bits, producing sharp, well-defined shoulders in dados and dovetails.
How it compares: Sapele is slightly harder and can have ribbon-stripe interlocked grain
that tears out if planed against the grain, but for sawing, dadoing, and slot cutting, it
feels almost identical to genuine mahogany.
3. Soft Maple (Red Maple / Silver Maple)
Cost: Moderately cheap, readily stocked at hardwood suppliers.
Machining Behavior: Holds ultra-crisp edges in narrow kerfs without splintering or tear-
out.
How it compares: Slightly harder than mahogany, but its uniform closed grain lets you
practice delicate joinery, narrow divider slots, and dovetails with high precision.
4. Clear Radiata or White Pine (Skip construction-grade yellow pine)
Cost: Inexpensive.
Machining Behavior: Fast to cut, but soft.
How it compares: The pronounced difference between soft springwood and hard
latewood can cause hand chisels to wander or tear out across grain lines. Useful for
quick gross-dimension proof-of-concepts, but less forgiving for fine, tight kerfs.
Recommended Approach
1. Poplar or scrap pine for the first dry run: Use 1/2" or 3/4" poplar to dial in table saw fence
stops, check divider slot spacing against your cast plaster tiles, and test corner joinery.
2. African Mahogany / Sapele for the finished build: If you want the authentic look and pitch-
resistant stability of mahogany without the genuine CITES-regulated price, African mahogany
or Sapele offers an excellent balance of cost, workability, and durability.
Sources
1. Is poplar a good body wood? : r/Luthier - Reddit
2. Mahogany Wood Comparison of Sapele, African Mahogany, Sipo
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 59/92
User prompt: Poplar it is! I think sizing a 12” long trough for practice joinery holding 4” bipolar
sheets. I really want to try dovetails but they terrify me
Response: Dovetails have an intimidating reputation, but on a straight box with four corners, they
are simply a series of straight saw cuts and light chisel work. Poplar is forgiving to learn on: it pares
cleanly across the grain without tearing out like pine or dulling your edges like rock maple.
The Secret to Stress-Free Dovetails: "Tails First"
Cutting the tail board (usually the long sides) first gives you a physical, 1:1 marking template to
scribe the pins directly onto the mating pin board. You never have to measure angles or pin spacing
twice.
       TAIL BOARD (Cut First)                 PIN BOARD (Marked From Tails)
       +-----+       +-----+                  +-----+                 +-----+
       |     \       /     |                  |     /                 \     |
       |      \     /      |       ======>    |    /    [ PINS ]       \    |
       |       \   /       |  (Scribe lines)  |   /                     \   |
       |        \ /        |                  |  +-----------------------+  |
       +---------+---------+                  +--+                       +--+
A 5-Step Beginner Workflow
1. Mark the Baseline Accurately:
Set a wheel marking gauge to the exact thickness of your mating board (or a hair
thicker, so pins end up proud for flushing later).
Scribe this depth line all the way around all four ends of every board. Never cut past
this line.
2. Lay Out Simple, Wide Tails:
Don't make microscopic, violin-maker pins on your first box. For a ~4.5" high trough, use
2 or 3 wide tails.
A classic 1:6 or 1:8 slope (roughly  to ) is standard. You don't need a fancy gauge
—draw a 1" offset over 6" on a scrap card to set a sliding bevel.
3. Saw to the Waste Side of the Line:
Clamp the tail board vertically in the vise.
Make your angled cuts down to the baseline. Keep the saw blade strictly on the waste
side of your pencil/knife line.
4. Clear the Waste:
Use a coping saw or fret saw to remove the bulk of the waste between the tails in one
quick U-shaped cut just above the baseline.
7∘ 9∘
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 60/92
Place a sharp bench chisel directly in your scribed baseline and pare flat to clean the
bottom floor.
5. Transfer to the Pin Board:
Clamp the pin board vertically in the vise. Lay the cut tail board flat on top, aligning the
edges flush.
Use a sharp marking knife or razor blade to trace the shape of the tails directly onto the
end-grain of the pin board.
Saw straight down on the waste side of those knife lines, clear the center with your
coping saw/chisel, and test fit.
Three "No-Panic" Practice Tips
Leave Them Proud: Make your baseline ~0.5 mm deeper than the board thickness. When
assembled, the pins and tails will stick out slightly. Five seconds with a hand plane or 120-grit
sanding block flushes them down dead-flat and makes the joint look seamless.
Blue Tape Trick: If seeing the lines on poplar end-grain is tough, put a strip of blue painter's
tape across the end-grain, scribe your knife lines through it, and peel away the waste
sections. Saw right along the crisp blue tape edge.
Saw a Scrap First: Take two 4" offcuts of poplar and cut just one single tail and pin to get
the muscle memory down before touching your 12" trough sides.
User prompt: I think the sides need to be at least 5” high to accommodate the bottom 1/2” plus a
1/4” rim, and maybe a 1/4” deeper than the plates at the top? Printable template please
Response: Here is a visual dovetail layout generator tailored to your dimensions. You can adjust
the parameters, toggle guides, and hit Print 1:1 Scale Template to generate full-scale templates to
glue directly onto your poplar test pieces.
Vertical Stack Breakdown (5.0" Total Height)
Your sizing math works out cleanly to a standard 5-inch finished board height:
Section Height Purpose / Function
Top Air Gap 0.250"
(1/4")
Freeboard to prevent electrolyte sloshing and give room for
jumper clips.
Active Plate
Zone 4.000" (4") Full immersion height for your 4" square plates and cast plaster
tiles.
Pitch Floor Bed 0.250"
(1/4")
Monolithic layer of poured rosin/pitch cement sealing the floor
seam.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 61/92
Section Height Purpose / Function
Captured
Groove
0.250"
(1/4")
1/4" wide groove plowed into the side walls to capture the floor
board.
Bottom Rim 0.250"
(1/4")
Solid wood meat below the groove to prevent the bottom edge
from splitting out.
Total Board
Width 5.000" (5") Standard S4S 1x6 nominal stock (5.5" actual) ripped down to
5.0".
Step-by-Step Template Usage
1. Verify Printer Scale: Print the template from the widget. Measure the printed 1-inch check
bar with a steel rule before sticking it down. If it is slightly off, set your printer dialog to "Actual
Size" / 100% scale (disable "Fit to Page").
2. Adhere to End Grain: Cut the paper template out and attach it to your squared poplar ends
using a light mist of spray adhesive (or a standard purple glue stick—it washes off with warm
water).
3. Score the Baseline: Score your wheel marking gauge across the baseline right through the
paper into the wood before making your first saw cut.
4. Saw the Waste: Saw strictly in the crosshatched waste areas to leave your pencil/knife lines
intact.
User prompt: The template for tails goes on the face of the board?
Response: Yes, exactly—the tail template goes on the broad face of the board.
The layout logic follows this rule:
Tails (Face Pattern): The angled slopes ( ) live on the face of the board. The cut on the
end-grain is a simple  square line straight across the thickness.
Pins (End-Grain Pattern): The angled slopes ( ) live on the end-grain of the mating
board. The cut down the face is a  plumb line down to the baseline.
--- TAIL BOARD LAYOUT (Side Wall) ---
         Top Edge
    +-----------------------------------------------+
    |  \           /             \           /      |  <-- FACE OF BOARD
    |   \ [TAIL]  /    [WASTE]    \ [TAIL]  /       |      (Angled lines here)
    |    \       /                 \       /        |
----+-----\-----/-------------------\-----/---------+--
1 : 6
90∘
1 : 6
90∘
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 62/92
|   |      \   /                     \   /          |  <-- BASELINE (Thickness)
+---+-------+-+-----------------------+-+-----------+
            | |
            | +-- Sawn straight 90° across END GRAIN
            |
How to Apply and Cut the Tail Template
1. Align to the End: Glue the face template flat on the wide face of your poplar board, aligning
the top edge of the template flush with the cut end-grain.
2. Square Across the End-Grain: Use a small engineer's try-square or combo square to extend
pencil lines  straight across the top end-grain from each point where the angled tail
lines touch the edge.
3. Clamp Vertically in the Vise:
Look down at the end-grain: your saw stays perfectly vertical ( ) relative to the
board's thickness.
Look at the face: tilt your saw left or right to track the printed  angled line down to
the scribed baseline.
4. Skip Printing the Pin Template: Once the tails are cut and the waste is chiseled out, don't
use a printed paper template for the pin board. Simply rest the cut tail board on the pin
board's end-grain and trace the pins directly with a sharp knife. That guarantees a zero-
tolerance match even if your saw wandered slightly on the tails.
User prompt: I have a couple of pieces of radiata pine, 3/4”x 6”x36”. If I wanted to make one into a
dovetailed box with a lid and bottom recessed into rabbets, and longer than wide, what are my
dimensional options? Or do I need more than one piece of wood?
Response: To make the 4 walls, a lid, and a bottom, using two boards is vastly easier and gives
you full height, but one board is possible if you build a shallower box and resaw or edge-
glue the offcuts.
Option 1: Using ONE Single Board (Shallower Box)
A single 6"  36" board has  of surface area. To get all 6 faces (4 sides + top +
bottom), you must rip the board lengthwise into strips:
+-------------------------------------------------------------+
| Strip A (Walls, 2.75" high):  [ Long ] [ Long ] [Sh] [Sh]   |  <-- 36" long
+-------------------------------------------------------------+
| Strip B (Panels, 3.0" wide):  [Panel 1] [Panel 2] [Panel 3] |
+-------------------------------------------------------------+
90∘
90∘
1 : 6
× 216 sq inches
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 63/92
Ripping: Rip the 6" width into Strip A (2.75" wide) and Strip B (~3.0" wide) (accounting for
blade kerf).
The 4 Walls (from Strip A):
2 Long sides: 10.5" long  2.75" high
2 Short sides: 6.5" long  2.75" high
Perimeter:  (leaving 2" for crosscut kerfs and
squaring).
Lid and Bottom (from Strip B):
Crosscut Strip B into three 11" lengths.
Edge-glue two pieces together to make a  panel for the lid (or resaw 3/4"
stock into two 5/16" thin boards on a bandsaw/table saw to get both top and bottom).
Final Box Dimensions:
Outside: 
Inside (with 3/4" walls): 
Option 2: Using TWO Boards (Full Height, Minimal Hassle)
Using two boards eliminates awkward edge-gluing and gives you the depth needed for a 5" tall
battery trough, tool chest, or storage box:
Board 1 (All 4 Walls):
Kept at full 5" to 6" width.
Crosscut directly into:
2 Long sides: 11.5" long  5.0"–6.0" high
2 Short sides: 6.0" long  5.0"–6.0" high
Total length:  (clean fit within 36").
Board 2 (Lid, Bottom & Test Pieces):
Crosscut two 11.5" lengths at full 6" width for the Lid and Bottom.
Leaves a 13" scrap piece to practice cutting dovetail joints before touching the box
pieces.
Final Box Dimensions:
×
×
10.5 + 10.5 + 6.5 + 6.5 = 34.0"
6.0" × 11.0"
≈ 10.5" L × 6.5" W × 2.75" H
≈ 9.0" L × 5.0" W × 1.75" H
×
×
11.5 + 11.5 + 6.0 + 6.0 = 35.0"
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 64/92
Outside: 
Inside:  (with 1/2" recessed floor and lid).
Comparison & Recommendation
Approach Max Outer Dimensions (
) Woodworking Required Practice Scrap Left
Over?
1 Board Rip cuts, edge-gluing or
resawing
None (zero margin for
error)
2 Boards Simple crosscuts only 13"  6" offcut for
practice joints
Recommendation: Use two boards. It gives you a proportioned  box that can hold 4"
battery plates or tools, avoids edge-gluing thin panels, and gives you a 13" offcut to practice your
first test dovetails.
User prompt: I’m just reading a translation of parts of Volta’s original 1880 paper. It seems like he
used himself as the voltmeter?! He also describes “I dispose, therefore, a row of several basons or
cups of any matter whatever, except metal, such as wood, shell, earth or rather glass (small
tumblers or drinking glasses are the most convenient), half filled with pure water, or rather salt
water or ley: they are made all to communicate by forming them into a sort of chain, by means of so
many metallic arcs, one arm of which, [Aa], or only the extremity [A], immersed in one of the
tumblers, is of copper or brass, or rather of copper plated with silver; and the other, [Z], immersed
into the next tumbler, is of tin, or rather of zinc.” what is ley?
Response: “Ley” is the archaic 18th-century spelling of lye—a strongly alkaline solution
historically made by leaching wood ashes with water (primarily potassium carbonate and potassium
hydroxide, or potash).
Volta noted that salt water or ley worked far better than pure water because the dissolved ions
dramatically lowered internal electrolyte resistance. (As an aside, his landmark letter to the Royal
Society was published in 1800, establishing the dawn of continuous electrochemistry).
Volta Literally Used Himself as the Voltmeter
You read that right: Alessandro Volta was his own detector and voltmeter.
In 1800, electrical meters for continuous direct current simply did not exist. Electrostatic tools like
the gold-leaf electroscope could only detect high static voltages (often requiring Volta’s own
"condenser" plate to see even a faint twitch from a chemical cell). To measure current, intensity,
and polarity, Volta turned to his own nervous system:
≈ 11.5" L × 6.0" W × 5.5" H
≈ 10.0" L × 4.5" W × 4.0" H
L × W × H
10.5" × 6.5" × 2.75"
11.5" × 6.0" × 5.5" ×
11.5" × 6"
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 65/92
The Tongue (Low-Voltage Sensor): To test 1 or 2 bimetallic couples (around , well
below the threshold of skin sensation), he touched the metal ends to the tip and base of his
moist tongue. He evaluated voltage by the sharpness of the acidic/sour taste (at the zinc
anode) versus an alkaline/soapy taste (at the copper/silver cathode).
The Eyes (Visual Phosphenes): By placing one lead in his mouth and touching the other to
his eyelid or forehead, the sudden make-and-break of the circuit stimulated the optic nerve,
producing a brief flash of light (phosphene) whose brightness indicated circuit vigor.
Fingers in Saline Cups (Shock Intensity / High Voltage): For larger piles of 20, 40, or 60
pairs ( ), he dipped his fingers or whole hands into bowls of salt water
connected to the pile terminals. He quantified the "force" of the pile by where he felt the
continuous prickling shock: whether the sensation stopped at the knuckles, traveled up to the
wrists, or jolted his forearms and elbows.
The "Crown of Cups" (Couronne de Tasses)
The passage you quoted describes Volta's Crown of Cups, which he introduced in that same
paper as the horizontal, non-draining alternative to his vertical "Pile":
    [ Tumbler 1 ]             [ Tumbler 2 ]             [ Tumbler 3 ]
   +-------------+           +-------------+           +-------------+
   | (Salt Water)|           | (Salt Water)|           | (Salt Water)|
   |             |           |             |           |             |
   |   [Cu]      |           |   [Cu]      |           |   [Cu]      |
   +----+--------+           +----+--------+           +----+--------+
        |                         |                         |
        +========[ Arch ]=========+========[ Arch ]=========+
                  (Zn-Cu)                   (Zn-Cu)
Instead of wet paper discs that dried out or squished together under the weight of a vertical pile, he
bent bimetallic strips of copper/brass and zinc into inverted U-arches and dropped them into
drinking glasses filled with brine or lye.
This horizontal layout was the direct ancestor of Cruickshank's trough battery (which fused the cups
into a single slotted wooden box) and Daniell's two-fluid cell decades later.
User prompt: The attached pdf is the original Volta paper. Can you give me a translation?
Response: An English translation of Alessandro Volta’s landmark letter to Sir Joseph Banks,
published in the Philosophical Transactions of the Royal Society of London (1800):
XVII. On the Electricity excited by the mere Contact of conducting
Substances of different kinds.
In a Letter from Mr. Alexander Volta, F.R.S., Professor of Natural Philosophy in the University
of Pavia, to the Rt. Hon. Sir Joseph Banks, Bart. K.B., P.R.S.
1 to 2 V
20 to 60 +  V
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 66/92
Read June 26, 1800.
Como in the Milanese, March 20, 1800.
After a long silence, for which I shall offer no excuse, I have the pleasure of communicating to you,
Sir, and through you to the Royal Society, some striking results at which I have arrived in pursuing
my experiments on the electricity excited by the mere mutual contact of metals of different kinds,
and even by that of other conductors, also differing among themselves, whether liquids or
containing some moisture to which they properly owe their conducting power.
The principal of these results, which encompasses nearly all the others, is the construction of an
apparatus that resembles in its effects—that is to say, in the shocks it can impart to the arms, etc.—
the Leyden jar, and even better, weakly charged electrical batteries, which would nevertheless act
unceasingly, and whose charge after each explosion restores itself; which enjoys, in a word, an
inexhaustible charge, a perpetual action or impulse on the electric fluid. But it differs essentially
from them both by this continual action peculiar to it, and because, instead of consisting like
ordinary Leyden jars and batteries of one or more insulating plates in thin layers (substances
supposed to be the only electrics) armed with conductors, this new apparatus is formed solely of
several of these latter bodies, chosen even from among the best conductors, and therefore the
most remote, according to what has always been believed, from an electrical nature.
Yes, the apparatus of which I speak, and which will doubtless astonish you, is nothing but an
assembly of a number of good conductors of different kinds arranged in a certain manner. Thirty,
forty, sixty pieces or more of copper, or better of silver, each applied to a piece of tin, or what is
much better, zinc, and an equal number of layers of water or some other liquid that is a better
conductor than plain water, such as salt water, lye (lessive), etc., or pieces of cardboard, skin, etc.,
well soaked in these liquids; such layers being interposed between each couple or combination of
the two different metals—such an alternating series, and always in the same order, of these three
kinds of conductors: that is all that constitutes my new instrument.
This instrument imitates the effects of Leyden jars or electrical batteries by giving the same shocks;
it falls, in truth, far below the activity of said batteries charged to a high degree as to the force and
noise of the explosions, spark, and distance at which the discharge can occur, equaling only the
effects of a battery charged to a very feeble degree, though having an immense capacity; but it
infinitely surpasses the power of these batteries in that it does not need to be charged in advance
by means of extraneous electricity, and is capable of giving shocks whenever it is touched properly,
however frequent those contacts may be.
This apparatus—similar fundamentally, as I shall show, and even in form, to the natural electrical
organ of the torpedo, electric eel, etc., far more than to the Leyden jar—I would like to call the
Artificial Electric Organ. And is it not composed solely of conducting bodies? Is it not active of
itself, without any previous charge, without the aid of any electricity excited by known methods,
acting unceasingly, and capable at every moment of giving shocks, which, when frequently
repeated or continued, produce that same numbness of the limbs that the torpedo causes?
Construction of the Vertical Column (The Pile)
I provide myself with several dozen small round plates or discs of copper, brass, or better silver,
about an inch in diameter (such as coins), and an equal number of plates of tin, or much better
zinc, of roughly the same shape and size. Exact precision is not required. I prepare, moreover, a
sufficient number of discs of cardboard, leather, or other spongy matter capable of absorbing and
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 67/92
retaining much water or liquid. These wet discs I make a little smaller than the metal discs, so that
when interposed, they do not project beyond them.
Having all these pieces ready—the metal discs clean and dry, and the non-metallic ones soaked in
plain water or, much better, salt water, and lightly wiped so they do not drip—I place horizontally on
a table one of the metal plates, for example silver, and on this first I adapt a second of zinc; upon
this second I lay a wet disc; then another silver plate, followed immediately by another of zinc,
succeeded again by a wet disc. I continue in this same manner, coupling a silver plate with one of
zinc, always in the same order (silver below, zinc above, or vice versa), interposing a wet disc
between each pair, building a column as high as can stand without falling.
If it contains about 20 of these pairs, it will already be capable of affecting Cavallo’s electrometer
(aided by the condenser) beyond 10 or 15 degrees, charging this condenser by a single touch so
as to give a spark, and striking the fingers touching its two ends (the head and foot of the column)
with small shocks.
To obtain these shocks, the fingers must be moistened with water so the skin is well soaked. To
receive stronger shocks, one connects the bottom plate of the column with a basin of water in
which one plunges one hand, while touching the top plate with a metal blade held firmly in the other
wet hand. Touching successively the 3rd, 4th, 6th, and up to the 20th pair, the shocks increase
gradually in strength, extending through the whole finger, the wrist, and even up to the elbow.
The Role of Electrolytes and Surface Area
The exact and extended contact of the wet discs is very important. While the metal plates need only
touch at a few points (being excellent conductors), liquids and moist bodies are far less perfect
conductors, requiring ample surface contact with the metals and one another so the electric fluid
may pass without excessive resistance, especially when moved with such weak force.
The effects are considerably more sensible as the temperature is warmer, since heat renders water
more conductive. But what makes it much better still are salts, particularly common salt.
If to the 20 pairs one adds 20 or 30 more, the shocks will extend through both arms to the
shoulders, leaving the arm numbed if contacts are repeated rapidly.
The "Crown of Cups" (Couronne de Tasses)
I will now describe another form, which differs most in shape from the column, but which has the
disadvantage of being more voluminous: the apparatus I call the Crown of Cups (Plate XVII, Fig.
1).
We arrange a row of several cups or goblets of any non-metallic matter (small drinking glasses are
most convenient), half filled with salt water or lye. We link them all in a chain by means of metallic
arcs, one arm  (immersed in one glass) being copper, brass, or silver-plated copper, and the
other  (in the next glass) being tin, or better zinc.
(I observe here that lye and alkaline liquors are preferable when tin is used; salt water is preferable
when zinc is used).
The two metals of each arc are soldered together above the liquid. The submerged parts should
have an area of about one square inch; the rest of the arc may be as narrow as desired, even a
Aa
Z
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 68/92
simple wire.
A series of 30, 40, or 60 of these glasses forms this new apparatus, which in substance is identical
to the column. Shocks are felt by plunging one hand into the first vessel and the other into the last.
Volta notes that if 60 cups are arranged in three groups of 20 with the middle 20 reversed in
polarity, the shocks weaken and cancel out around the 40th cup before rising again at the 60th,
demonstrating that the electromotive forces add algebraically.
Multi-Column Piles and Durability (Plate XVII, Figs. 2, 3, 4)
To make tall columns stable, Volta describes enclosing them within 3 or 4 vertical guide rods (
) of glass or insulated wood (Fig. 2), or dividing the battery into multiple connected sub-
columns (Figs. 3 & 4) linked by metal strips ( ).
To prevent the wet discs from drying out after a day or two, he recommends coating or potting the
entire assembled cylinder in wax or pitch (enveloppant de cire ou de poix toute la colonne).
Sensory Effects on the Human Body
Volta details how continuous direct current affects the senses:
Touch & Continuous Pain: When a wire from a 40–50 pair pile is pressed to moist skin
(forehead, eyelid, or nose tip), there is an initial prickling shock upon making contact. If the
circuit remains closed without interruption, this is followed by a persistent, sharp, burning pain
that increases until it becomes unbearable. This proves the continuous, sustained circulation
of the electric fluid. The pain is even more acute on broken skin, burns, or small cuts.
Taste: Testing with zinc and silver on the tongue produces a distinct acidic/sour taste when
the current enters the tip of the tongue (negative polarity), and an alkaline/soapy/acrid taste
when the current leaves it. With 30–40 pairs, an immediate muscular convulsion and sharp
prickle accompany the taste.
Sight: Connecting the circuit across the moist face, eyelids, or mouth produces an
instantaneous flash of light or luminous circle in the eyes upon making/breaking the loop.
Hearing: Inserting two blunt metal rods deep into the ears and completing a 30-to-40-pair
circuit produced a shock in the head, followed by a continuous crackling, bubbling, or boiling
noise (like a thick paste boiling) that persisted as long as the circuit remained closed. Volta
noted this sensation was disagreeable and feared it was dangerous, so he did not repeat it
often.
Smell: Attempting to stimulate the nose produced only localized stinging rather than any
scent, because the electric fluid was contained in liquid conductors rather than discharging as
a spark/effluvium through the air.
Conclusion: Refuting "Animal Electricity"
Volta concludes by examining the anatomy of the torpedo fish. He argues that William Nicholson’s
theory—that the fish's organ consists of tiny insulating talc plates acting as electrophores—is
mmmm
cc
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 69/92
impossible because living tissue is moist and conductive, incapable of holding electrostatic
charges.
The torpedo's organ operates under the exact same principle as his own column: a large stack of
conductive disks of differing materials whose mutual contact generates and sustains an electric
current.
User prompt: He mentions using “Cavallo’s electrometer” with a condenser, can you explain that?
Response:
Tiberius Cavallo’s Electrometer: A 18th-century sensitive device utilizing two small pith balls
hung on fine linen threads or silver wires inside a glass bottle to detect small static charges.
When charged, the pith balls repel each other, with the angle of separation indicating the
voltage intensity.
The Condenser (Capacitor) Attachment: Because early chemical cells produced very low
voltage (~1.1 V per cell) that was too weak to move pith balls directly, Volta attached a
"condenser"—two insulated parallel brass discs separated by a thin layer of insulating varnish
or resin.
Accumulating the Charge: By connecting one terminal of the pile to the lower disc and
grounding the upper disc for a few moments, the condenser absorbed and stored the
continuous current, accumulating minute amounts of charge over time.
Reading the Result: When the user quickly lifted the upper disc by its insulating handle, the
capacitance dropped drastically, instantly multiplying the trapped voltage to a high enough
potential to force Cavallo's pith balls to diverge past 10 or 15 degrees, making the weak
current visible.
User prompt: Cavallo’s paper mentions an electro phosphorous?
Response: An electrophorus (often spelled "electrophorus" or historically referred to with variants
like electrophore) is a simple manual electrostatic generator invented in the late 18th century. It
consists of an insulating resin plate and a metal plate with an insulating handle.
When the resin plate is rubbed to charge it via friction, the metal plate is placed on top, briefly
touched to ground to drain induced charge, and then lifted away by its handle. The metal plate
carries away a strong static charge via electrostatic induction without depleting the original charge
on the resin, allowing the process to be repeated indefinitely.
In Volta's 1800 paper, he uses "electrophorus" and "condenser" concepts interchangeably in
discussions regarding how static instruments function, and he heavily critiques contemporary rival
theories (such as William Nicholson's) that attempted to model biological electric organs or
chemical piles as networks of tiny built-in electrophores.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 70/92
User prompt: What material was used to make the resin plate?
Response: The insulating plate (often referred to as the "cake") of an electrophorus was typically
formed using a mixture of shellac and resin, or a specialized blend of resinous materials, wax,
and turpentine spread over a base plate.
Alessandro Volta and other 18th-century experimenters favored these specific resinous
compositions because they possessed exceptional dielectric properties, held a strong triboelectric
negative charge when whipped or rubbed with fur, and retained that electrostatic charge for long
periods without leaking away.
User prompt: I don’t understand why the metal is connected to ground after being placed on the
charged resin? Wouldn’t that drain all the charge to ground?
Response:
Electrostatic Induction: The charged resin plate creates an electric field that polarizes the
metal plate placed on top of it, driving free electrons to the top surface while leaving a positive
charge on the bottom surface facing the resin.
The Grounding Step: Connecting the metal plate to ground momentarily provides a path for
those excess electrons on the top surface to escape into the earth, but the positive charge on
the bottom remains trapped because it is held in place by the electrostatic attraction of the
negative resin.
Trapped Charge Retention: The resin's own bound charge does not drain to ground
because the resin is an insulator; the ground connection only interacts with the free electrons
on the metal sheet.
Lifting the Plate: Once you break the ground connection and lift the metal plate away by its
insulating handle, the net positive charge is trapped on the metal, giving you a high-voltage
charge to use elsewhere while leaving the original resin cake completely untouched and
ready to repeat the process.
User prompt: And this charge could be transferred to a capacitor in the form of a Leyden jar or
something similar?
Response:
Direct Transfer: Yes, lifting the charged metal plate and touching its edge to the knob of a
Leyden jar transfers a small packet of high-voltage static electricity.
Cumulative Charging: Because the underlying resin cake does not lose its charge when the
metal plate is lifted, you can repeat the sequence—place the plate, touch ground, lift, and
touch the Leyden jar—dozens of times.
Building a Charge: Each cycle dumps another increment of charge into the Leyden jar,
allowing you to accumulate a large static charge from a single initial rubbing of the resin cake.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 71/92
User prompt: Earlier you mentioned condensers made of brass plates separated by varnish. I
couldn’t find any pictures like that?
Response: Historic images or search results for these specific devices are usually labeled under
"Volta's capacitor" (or condensatore elettrico) and "Volta's condensing electrometer"
(elettroscopio condensatore) rather than modern electronic capacitors.
In museum collections—such as the Tempio Voltiano in Como, Italy—these apparatuses typically
look like:
Two polished circular brass plates.
The lower plate sits fixed on an insulating glass or resin-coated pedestal.
The upper plate (the "shield") features an insulating glass or varnished handle extending
upward.
Instead of modern plastic or ceramic dielectrics, the inner faces of the brass plates were
lightly coated with an insulating layer of shellac varnish, resin, or sealing wax. This thin
organic film prevented the bare metal faces from making direct galvanic or metallic contact
when pressed together, maintaining a microscopic air and resin gap so static charges could
"condense" via electrostatic induction.
User prompt: What recipe would Volta have used for the resin disks in his perpetual electrophore?
Response: Volta and 18th-century instrument makers did not use a single rigid chemical formula for
the electrophorus resin cake, instead relying on combinations of natural resins, drying oils, and
waxes melted together and poured into a shallow wooden or metal base.
The Core Ingredients: The mixture typically combined shellac (for hardness and triboelectric
charge retention) with pine rosin (colophony) and a small amount of Venice turpentine or
beeswax to prevent the cake from becoming too brittle and cracking as it cooled.
Proportions: A standard historical compounding ratio hovered around 2 parts shellac to 1
part rosin, with just a few drops to a tablespoon of turpentine or wax added to plasticize the
mixture.
Preparation Method: The ingredients were melted together slowly in an iron crucible over
low heat until completely liquefied, ensuring no water was trapped inside. The molten resin
was then poured directly into a shallow circular wooden or metal pan (the scutella) to a depth
of roughly 1/4 to 1/2 inch, where it solidified into a smooth, dark, highly insulating cake.
Come costruire un elettroforo di Volta
This video demonstrates a simple, modern replica of Volta's electrophorus using easily accessible
household materials to illustrate the principles of electrostatic induction.
http://googleusercontent.com/youtube_content/1 YouTube video views will be stored in your
YouTube History, and your data will be stored and used by YouTube according to its Terms of
Service
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 72/92
User prompt: What is Venice turpentine and how was it made in the 18th and 19th centuries?
Response: Venice turpentine (also known as Venetian turpentine or larch balsam) is a thick,
transparent, golden-yellow oleoresin. Despite its misleading name, it is not a distilled liquid solvent
like modern gum turpentine; rather, it is the raw, viscous, honey-like sap of the European larch tree
(Larix decidua). It earned its name because Venice served as the primary historic trading hub and
gateway through which the resin was distributed across Europe.
Historical Harvesting Methods (18th–19th Centuries)
During the 18th and 19th centuries, harvesting larch resin was a specialized trade concentrated
heavily in the alpine forests of Austria, the Tyrol, and northern Italy.
The Drilling Technique: Unlike pine resin harvesting—which often involved stripping large
sections of bark—larch harvesting relied on a specialized drilling method to tap the
heartwood. Harvesters drilled an upward-slanting hole deep into the lower trunk of mature
larch trees (usually between 1,000 and 1,300 meters above sea level) to reach the resin-
bearing canals.
Collection Tubes: A small wooden plug or hollow tube (often reed or elderberry pith) was
inserted into the drilled hole to channel the slow-flowing, viscous balsam directly out of the
tree.
Harvesting and Sealing: Harvesters (historically referred to in regional traditions as drop
hunters or woodsmen) periodically returned with small wooden casks or copper vessels to
collect the accumulated resin. Once harvest season ended, the hole was plugged with a
wooden peg or sealed with pitch to let the tree heal.
Refining: The raw exudate was strained through coarse linen cloth to remove bits of bark,
dirt, and wood dust, yielding a pure, honey-like balsam that retained its natural essential
volatile oils without requiring artificial distillation.
Larch Venice Turpentine - A Resin Not A Solvent
This short video provides a quick visual overview of what Venice turpentine looks like and clarifies
its true nature as a thick, viscous tree resin rather than a liquid solvent.
http://googleusercontent.com/youtube_content/1 YouTube video views will be stored in your
YouTube History, and your data will be stored and used by YouTube according to its Terms of
Service
User prompt: And was the shellac the same material as modern shellac used as a wood finish?
Response: Yes, it is fundamentally the exact same material.
Modern shellac flakes used by woodworkers today are still harvested from the exact same source:
the secretion of the tiny lac bug (Kerria lacca) gathered from forest trees in India and Southeast
Asia.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 73/92
The primary differences between what Volta used for his electrophorus cakes and what you buy in
a woodworking shop today come down to processing and additives:
Natural Wax Content: Raw, unprocessed shellac naturally contains about 3% to 5% natural
insect wax. For an 18th-century electrophorus cake or sealing wax, this natural wax was
actually welcomed because it added flexibility and moisture resistance. For modern wood
finishes, manufacturers often put the flakes through a chemical process to yield dewaxed
shellac, which provides better clarity and allows subsequent topcoats (like varnish or
polyurethane) to adhere properly.
Color and Bleaching: Historically, shellac came in deep ambers, browns, and oranges
(commonly called "orange shellac") because of the twigs, tree sap, and natural pigments
embedded in the raw resin. Modern woodworkers often use "blonde," "super blonde," or
platinum grades that have been chemically bleached or filtered through activated carbon to
remove those color bodies.
Intended Use vs. Formulation: While woodworkers dissolve shellac flakes in denatured
alcohol to brush, wipe, or French-polish onto timber, Volta melted his flakes directly with rosin
and turpentine into a thick, rigid structural mass meant to be poured solid into a mold.
User prompt: Is there any reason to prefer pine rosin that is already powdered over flakes or
chunks in this application?
Response:
Faster Melting: Powdered rosin has an immensely higher surface-area-to-volume ratio than
large chunks or blocks, allowing it to liquefy almost instantly when heated in the crucible
alongside shellac and Venice turpentine.
Easier Proportioning: Fine powder can be measured by volume or weighed out precisely
without needing a hammer or chisel to break down stubborn, glassy chunks of raw pitch.
Dust and Explosion Hazard: Powdered rosin carries a severe airborne dust hazard; in a hot
workshop or near an open flame used to melt the mixture, fine pine rosin dust is highly
combustible and can flash or ignite explosively.
Oxidation: Powdered rosin has vastly more surface area exposed to ambient air, making it
more prone to oxidation and moisture absorption over time compared to dense, solid blocks
or flakes.
Recommendation: Chunks or coarse flakes are generally preferred for this application. They melt
down smoothly with minimal stirring while completely avoiding the explosive dust and rapid
oxidation risks associated with fine powder.
User prompt: I found some “larch gum” that says it is made from the resin of larch trees. Larch
turpentine returns results of distilled gum turpentine and Venice turpentine the same or a horse
remedy for coating hooves
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 74/92
Response: Larch gum (often sold under names like American larch gum or larch arabinogalactan)
is chemically different from Venice turpentine and gum turpentine.
Larch Gum (Arabinogalactan): This is a water-soluble polysaccharide extracted from the
wood of western larch trees (Larix occidentalis). It dissolves completely in water and acts as a
binder, dietary fiber, or emulsifier, but it has no resinous, sticky, or waterproofing properties
when dry.
Venice Turpentine (Oleoresin): As discussed earlier, this is the raw, sticky oleoresin tapped
directly from the heartwood of the European larch tree (Larix decidua). It is hydrophobic,
viscous, and soluble in solvents like spirits of turpentine or alcohol, making it suitable for
hardening resin blends.
Distilled Gum Turpentine: This is the volatile solvent fraction produced by steam-distilling
raw pine or larch tree resins, yielding a thin liquid spirit used for thinning paints and varnishes.
The Hoof Remedy Connection: The horse hoof remedy reference comes from historical
veterinary practices where thick larch or pine turpentines were painted onto equine hooves to
provide a flexible, waterproof barrier against moisture and thrush.
What you need for an electrophorus cake: You need an oleoresin or balsam (like genuine Venice
turpentine) rather than water-soluble larch gum or distilled liquid gum turpentine.
User prompt: So the horse hoof coating is the closest? Could i use beeswax to plasticize the cake
instead? I am not sure about the nature of these other products though at least one is described as
an oleoresin
Response: Yes, beeswax is historically correct and works well as a plasticizer.
While Venice turpentine adds a sticky, tacky flexibility, 18th-century makers and modern historical
craftsmen frequently used pure beeswax or tallow to soften brittle resin-and-shellac blends and
prevent them from cracking under mechanical stress.
The Equine Connection: The reason the horse hoof coating matches chemically is because
historical veterinary "Venice turpentine" was authentic larch oleoresin; because horseshoes
and hooves needed a flexible, waterproof dressing that wouldn't wash off in mud, the exact
same raw balsam harvested from the Alps was sold for both artistic/pharmaceutical and
veterinary uses.
Beeswax vs. Turpentine: Beeswax will make the cake slightly softer and less sticky than
turpentine, so you only want to use a small proportion (roughly 5% to 10% by weight of the
total shellac/rosin mix) to avoid making the surface too soft to hold a static charge.
User prompt: I noticed that Cavallo’s electrometer and Volta’s capacitor electrometer both have
sealing wax on the top neck of the glass bottle. What’s the value of that?
Response: Sealing wax on the neck of an electrometer bottle acts as an absolute moisture
barrier and mechanical anchor.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 75/92
Preventing Surface Leakage: Glass readily attracts an invisible microscopic film of moisture
from ambient air. This moisture creates a conductive path that allows static charges to bleed
away into the air or down the outside of the bottle, destroying the instrument's sensitivity.
Hermetic Insulation: Sealing wax is a hydrophobic, high-dielectric resin blend. Melting it
around the neck where the metal support rod or cork enters the glass hermetically seals the
joint against humidity.
Mechanical Stability: It rigidly locks the internal suspension wire, brass rod, or hook in place,
preventing it from shifting or rotating when the instrument is handled or connected to a
charging lead.
User prompt: That’s … interesting. Some versions of electrometer used gold leaf. Could that be
replaced with aluminum foil?
Response: Aluminum foil works mechanically, but its high mass creates severe operational
limitations compared to traditional gold leaf.
Weight and Thickness: Standard household aluminum foil is roughly 0.016 mm (16 microns)
thick and weighs about . Historical gold leaf used in electrometers was hammered
down to roughly 0.0001 mm (0.1 microns)—over 100 times thinner—and weighed a fraction of
a gram per square meter.
Inertial Resistance: Because aluminum foil is vastly heavier and stiffer, it requires a much
stronger electrostatic charge to overcome its own mass and push the leaves apart, making
the electrometer significantly less sensitive to weak static fields.
Tearing and Creasing: Gold leaf behaves almost like a fluid sheet, fluttering smoothly under
minute electrical attractions. Aluminum foil tends to crease, kink, and hold rigid folds that
interfere with smooth divergence.
Practical Workaround: If you want to build a working replica without tracking down genuine gold
leaf, look for ultra-thin aluminum condenser microphone diaphragms, extremely thin metallic
gift-wrapping foil, or carefully split multi-layer foil wrappers, keeping the hanging strips as short and
narrow as possible to minimize weight.
User prompt: What about craft gold leaf sheets? Are they thin enough?
Response: Yes, craft gold leaf sheets can work, but you need to check whether you are buying
genuine gold craft leaf or imitation craft leaf (often called composition or Dutch metal), as their
physical properties differ significantly for an electrometer:
Genuine Craft Gold Leaf: If the craft book contains real gold (even lower karats like 12k or
22k), it is beaten down to roughly  thick. This is practically identical to
historical leaf and will perform wonderfully with extreme sensitivity.
Imitation Craft Leaf (Composition / Dutch Metal): Most cheap craft store "gold" or "silver"
leaf is actually an alloy of copper and zinc (for gold) or thin aluminum (for silver). While
43 g/m2
0.1 to 0.5 microns
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 76/92
genuine imitation gold is still quite thin (roughly ), it is noticeably stiffer,
heavier, and springs back rather than fluttering fluidly.
If you use imitation craft leaf, the electrometer will still work, but you will need a stronger
electrostatic charge to overcome the stiffness and mass of the strips compared to true beaten gold
leaf.
User prompt: So what is the difference between 24 carat and 12 carat?
Response:
Purity: 24-carat gold is 100% pure gold (or 24 parts out of 24), whereas 12-carat gold is only
50% pure gold (12 parts gold mixed with 12 parts of other metals like copper, silver, or zinc).
Properties: Because pure gold is extremely soft and malleable, 24-carat gold bends and
scratches easily. Mixing it down to 12-carat adds alloy metals that drastically increase
structural strength, durability, and scratch resistance.
Color and Workability: Lower-carat golds can vary in color (such as yellow, white, or rose)
depending on the specific alloy metals used, and they handle differently when beaten into
ultra-thin leaf or worked by a jeweler.
User prompt: Why would they put foil on the inside of the bottle?
Response:
Capacitance and Conduction: A Leyden jar requires both an inner and outer conductive
layer to act as the "armatures" (plates) of a capacitor, allowing opposite electrical charges to
accumulate on either side of the glass.
Charge Storage: The internal metal foil lining serves as the internal conductor that receives
and stores the charge introduced through the top chain or rod.
Glass as a Dielectric: The glass bottle itself acts as the insulating dielectric barrier, keeping
the charges separated until a discharge occurs.
User prompt: Oh I meant inside an electrometer.
Response:
Eliminating Internal Static Drag: The inside of an electrometer bottle is lined with strips or
patches of foil (or coated in conductive tinfoil/graphite) to create an equipotential Faraday
shield or to ground the interior glass walls.
Preventing Charge Sticking: Uncoated glass inside an electrometer can trap stray static
charges on its surface from induction, which then attract, pin down, or deflect the delicate gold
0.8 to 1.0 micron
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 77/92
leaves, causing erratic or stuck readings.
Controlled Grounding: In some designs (like Kelvin or quadrant electrometers), the interior
lining is connected to ground, ensuring that the leaves interact only with the central charge
terminal rather than unpredictable static fields clinging to the inner glass walls.
User prompt: I’m curious because that’s the only element that needs the bottom of the bottle
removed.
Response:
Grounding the Enclosure: Grounding strips or inner foil linings on an electrometer (such as
a Henley quadrant electrometer or specialized Henley-style designs) create a conductive
shield that protects the interior environment from erratic external electrostatic fields.
The Bottom-Removal Need: Constructing certain historical electrometers required removing
the bottom of a glass bottle or bell jar to physically install internal mounting fixtures, support
pillars, or graduated scale arcs that could not fit through the narrow neck.
Sealing It Back Up: Once the internal components, plumb lines, or indicator needles were
secured to the base or a bottom wooden/metal plate, the jar was sealed back up to maintain
an airtight, dust-free chamber protecting the delicate moving parts.
User prompt: What is type III glass? I can find some cheap round bottles.
Response:
Soda-Lime-Silica Glass: Type III glass is standard commercial soda-lime glass, which is the
most common and inexpensive glass used for everyday bottles, jars, and mass-produced
beverage containers.
Chemical Resistance: It has moderate hydrolytic resistance, meaning it is fine for general
liquids, foods, and many chemical solutions, but it can leach minor amounts of alkali into
highly sensitive or acidic reagents compared to lab-grade borosilicate (Type I).
Thermal Performance: It has a high thermal expansion coefficient, making it vulnerable to
thermal shock (cracking if heated or cooled too rapidly).
Affordability: Because it is mass-produced for commercial packaging, round Type III glass
bottles are widely available and extremely inexpensive, making them a practical choice for
bulk storage or DIY projects where extreme thermal shock or ultra-pure chemical inertness
isn't required.
User prompt: How easy is it to cut off the bottom of a glass bottle?
Response: Cutting the bottom off a standard Type III soda-lime glass bottle is moderately difficult
and requires patience, but it is entirely doable in a home workshop using a few standard methods.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 78/92
Because soda-lime glass is thermally sensitive, it behaves very differently than specialized
borosilicate glass.
Thermal Shock Scoring (The String Method): Wrap a flammable string (soaked in alcohol
or acetone) tightly around the bottle where you want the cut. Ignite the string, let the flame
heat the glass evenly for a minute, and then immediately plunge the bottle into a bucket of
cold water. The sudden thermal contraction often causes a clean crack to propagate along the
heated line, though the edge will be sharp and rough.
Scoring and Temperature Cycling: Score a continuous scratch around the circumference of
the bottle using a glass-cutting wheel or a diamond scribe. Alternately apply heat (using a
localized torch or boiling water) and a cold source (like an ice cube or cold damp sponge)
directly over the score line until the bottom thermal-fractures off.
Diamond Grit Tile Saw or Wet Saw: For the cleanest, straightest cut, use a wet tile saw
equipped with a continuous-rim diamond blade. Support the bottle carefully, feed it slowly into
the spinning blade with a steady stream of water cooling the cut, and let the diamond grit
grind through the soda-lime glass without forcing it.
Regardless of the method you choose, always wear eye protection and heavy gloves, and expect
to clean up the newly exposed edge with wet-dry silicon carbide sandpaper (around 80-grit to 220-
grit) to remove sharp burrs.
User prompt: These would all be possible with square bottles too.
Response:
Flat Surfaces: Square bottles provide flat exterior walls, making it significantly easier to
adhere conductive tinfoil or copper tape evenly to both the inside and outside when building a
square Leyden jar or capacitor.
Mechanical Stability: A square or rectangular cross-section prevents the vessel from rolling
around on the workbench during assembly, wiring, or mounting operations.
Internal Alignment: Flat inner walls allow internal foil linings or electrode plates to sit flush
against the glass without awkward curving air gaps.
Consistent Scoring: Using a glass-scoring tool or thermal wire on square glass requires
careful handling around the sharp 90-degree corners, as thermal cracks tend to wander
unpredictably away from rounded radii unless scored deeply.
User prompt: I was thinking about a wet tile saw
Response:
Clean, Flat Cuts: A wet tile saw with a continuous-rim diamond blade yields a perfectly
straight, square edge on glass bottles without the wandering thermal fractures common with
the string method.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 79/92
Corner Navigation on Square Bottles: Feeding a square bottle through a wet saw requires
you to rotate the bottle slowly through the blade at each 90-degree corner, letting the diamond
grit grind the flat face before navigating the radius.
Thermal Stress Management: The constant stream of cooling water on a wet tile saw
drastically minimizes local thermal stress, preventing the soda-lime glass from cracking
unpredictably during the cut.
Edge Cleanup: Even with a wet saw, the cut glass will leave a micro-serrated edge; always
back up the cut with wet-dry silicon carbide sandpaper (around 120-grit to 220-grit) lubricated
with water to ease the sharp rim.
User prompt: Ok I am thinking about the order in which I should reconstruct these things. Seems
like the electrophore is a good starting point, followed by a Leyden jar or electrometer, and a
capacitor.
Response: 1. Volta’s Electrophorus (The Generator) Starting here is essential because it
provides your primary, renewable source of electrostatic charge via induction. Without a reliable
way to generate static electricity, you cannot test or charge any subsequent apparatus.
2. Gold-Leaf Electrometer (The Detector) Building this second gives you an immediate tool to
visualize and measure the charges coming off your electrophorus. You need a sensitive detector to
confirm that your resin cake is charged, your metal plate is working, and your insulation is holding.
3. Leyden Jar (The Storage Tank) Tackling the Leyden jar third lets you capture and accumulate
the incremental charge packets generated by your electrophorus. It turns a momentary static spark
into a heavy, high-voltage jolt you can store and discharge at will.
4. Volta’s Condenser / Brass-Plate Capacitor (The Fine Instrument) Saving the multi-plate
brass condenser for last makes the most sense because it combines the principles of all the
previous devices. It relies on the induction concepts of the electrophorus, the storage principles of
the Leyden jar, and the detection sensitivity of the electrometer to demonstrate how minute charges
are "condensed" into measurable potentials.
User prompt: And then the voltaic pile, crown of cups, and trough battery. Or was there any other
experimentsin between voltas paper and the trough battery?
Response:
Simultaneous Reveal: In Volta’s famous March 1800 announcement letter to the Royal
Society of London ("On the Electricity Excited by the Mere Contact of Conducting
Substances"), he didn't just introduce the vertical voltaic pile—he debuted the crown of
cups (couronne de tasses) right alongside it in the exact same paper. He viewed them as two
configurations of the same underlying "apparatus of electromotive force."
The Intervening Gap: There were no major revolutionary battery architectures invented
between Volta's paper and the trough battery. Instead, the immediate aftermath of his 1800
publication triggered an explosion of replication, experimentation, and minor mechanical
refinements across Europe.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 80/92
The Trough Battery Evolution: The trough battery (or "trough validator") was actually
created shortly after by British chemist William Cruickshank in 1800/1801. Cruickshank
didn't change the chemistry; he solved a frustrating mechanical flaw of Volta’s vertical pile: the
extreme weight of tall stacks squeezed the brine out of the cardboard spacers, causing them
to dry out, leak conductive salts down the sides, and short-circuit. By cementing the
alternating copper and zinc plates vertically into slots inside a long, horizontal wooden trough
(creating water-tight compartments filled with acid or brine), he made a much more stable and
robust battery.
Sources
1. Electrochemistry Encyclopedia -- Volta and the "Pile"
2. Volta Invents the Battery | History | Research Starters - EBSCO
3. History of the battery - Wikipedia
User prompt: And the Daniel cell was the next big breakthrough?
Response: Solving Polarization The Daniell cell, invented by British chemist John Frederic Daniell
in 1836, was indeed the next major technological leap because it permanently solved the crippling
issue of polarization.
The Hydrogen Problem Volta’s pile, the crown of cups, and Cruickshank’s trough all suffered from
a shared operational flaw: during discharge, hydrogen gas bubbles accumulated and clung to the
copper plate. This insulating blanket of gas rapidly increased internal resistance and caused the
battery's voltage to plummet within minutes under a heavy load.
The Two-Fluid Breakthrough Daniell eliminated hydrogen gas entirely by splitting the cell into a
two-fluid system separated by a porous barrier (such as unglazed earthenware or an ox-gullet
membrane):
The Anode Side: A zinc rod immersed in a zinc sulfate or dilute sulfuric acid solution.
The Cathode Side: A copper plate or container immersed in a copper sulfate solution.
The Reaction: Instead of generating escaping gas, copper ions from the solution safely
plated themselves directly onto the copper electrode as pure metal, keeping the cell's
electrical output remarkably stable.
Impact on Infrastructure Because it was the first battery capable of providing a steady, continuous
current over hours and days rather than minutes, the Daniell cell became the absolute workhorse of
the 19th-century electrical revolution. It powered the expansion of global telegraph networks and
was even used as the voltage standard to help define the modern volt.
Sources
1. The Daniell Cell: A More Reliable Source of Electricity
2. Daniell Cell - Magnet Academy - National MagLab
3. Telegraph Batteries: Daniell and Grove Cells Explained - FlashFish
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 81/92
User prompt: Ox gullet! Is that the same as the cow tracheas available as dog treats?
Response: No, an ox gullet is the esophagus, whereas a cow trachea is the windpipe.
While both are tubular animal tissues commonly sold today as dehydrated dog chews, they differ in
both biological structure and historical function:
Ox Gullet (Esophagus): The esophagus is a muscular, flexible tube lined with a smooth
mucosal membrane. Historically, this muscular and fibrous tissue was cleaned, split open, and
dried to create thin, surprisingly tough, semi-permeable membranes. They were used for
everything from sausage casings to early biological diaphragms and porous partitions in
chemical cells.
Cow Trachea (Windpipe): The trachea is reinforced by rigid, horseshoe-shaped rings of
cartilage designed to keep the airway open against air pressure. While it is tubular, those stiff
cartilage rings make it entirely unsuitable for flattening out or using as a flexible, uniform
porous membrane in an electrochemical cell.
If you are looking to replicate an authentic porous barrier for a historical cell variant like an early
Daniell or porous-cup cell, a thin slice of unglazed earthenware (like a flowerpot saucer) or a
modern ceramic membrane will give you a much more predictable and stable barrier than organic
membranes.
User prompt: How about advances in measuring current?
Response: The evolution of current measurement mirrors the shift from qualitative detection to
precise, standardized engineering, moving alongside the battery breakthroughs of the 19th century:
The Oersted Effect & The "Multiplier" (1820): Immediately after Hans Christian Ørsted
discovered that a live wire deflects a compass needle, Johann Schweigger created the first
crude current detector by wrapping a coil of wire many times around a compass. Because the
turns multiplied the magnetic effect, early scientists called it a "multiplier".
The Tangent Galvanometer (1837): Developed by Claude Pouillet, this was the first truly
practical instrument for quantifying current. By aligning a vertical coil with Earth’s magnetic
field, the current passing through could be mathematically calculated based on the tangent of
the deflection angle of the needle.
The Mirror Galvanometer (Late 1850s): Invented by William Thomson (Lord Kelvin) to
detect extremely faint signals on the first transatlantic telegraph cables, this replaced physical
pointers with a tiny mirror and a beam of light. A microscopic twist of the suspended magnets
threw a light-spot across a distant scale, magnifying sensitivity by orders of magnitude.
The d'Arsonval Moving-Coil Meter (1882): Jacques-Arsène d'Arsonval revolutionized the
field by flipping the design: instead of a moving magnet affected by Earth's field, he used a
stationary permanent magnet and suspended a moving coil of wire. Soon commercialized
by Edward Weston, this laid the direct structural foundation for nearly all analog multimeters,
ammeters, and voltmeters used through the 20th century.
Sources
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 82/92
1. Galvanometer - Wikipedia
2. A Short History of the Galvanometer
3. Tangent Galvanometer - Washington and Lee University
4. Galvanometer - ELECTRIC WORLD
User prompt: What was the next battery breakthrough after the Daniel cell
Response:
The Grove Cell (1839): Invented by Welsh physicist William Robert Grove, this two-fluid cell
substituted the copper component of the Daniell cell with a platinum cathode immersed in
concentrated nitric acid. The nitric acid acted as a powerful depolarizer, dramatically lowering
internal resistance and boosting output voltage from 1.1 volts up to nearly 1.9 volts, making it
the premier power source for early telegraph lines despite emitting noxious nitric oxide fumes.
The Bunsen Cell (1841): German chemist Robert Bunsen made Grove’s high-voltage design
economically practical by replacing the expensive platinum cathode with cheap, molded
carbon blocks sourced from coal-gas retorts. This maintained the powerful output of the
Grove cell while slashing manufacturing costs.
The Lead-Acid Battery (1859): French physicist Gaston Planté created the world’s first
rechargeable (storage) battery. By submerging two spiral-wound lead sheets separated by
cloth into a bath of dilute sulfuric acid and running a charging current through them, he built a
cell that could store and return large surges of electrical energy. This direct ancestor of
modern automotive batteries solved the permanence problem of primary cells.
The Leclanché Cell (1866): Developed by French engineer Georges Leclanché, this cell
paired a zinc anode with a porous cup containing a manganese dioxide and carbon mixture,
using an ammonium chloride solution as the electrolyte. It was far more stable, portable, and
user-friendly than its predecessors. Its later refinement into the 19th-century "dry cell" enabled
the mass commercialization of portable consumer electronics.
Sources
1. Battery - Rechargeable, Storage, Power | Britannica
User prompt: The le clanche cell wasn’t rechargeable
Response: The Leclanché cell is indeed a primary, single-use battery rather than a rechargeable
secondary cell.
While Planté’s lead-acid battery solved the rechargeability problem a few years earlier, it was
heavy, hazardous, and impractical for low-drain household devices. The Leclanché cell traded
rechargeability for sheer practical convenience:
Stable Shelf Life: Because its components remained chemically stable when the circuit was
open, it didn't self-discharge rapidly like earlier wet cells.
Lower Maintenance: It replaced aggressive acids with a milder ammonium chloride solution.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 83/92
The Dry Cell Evolution: Its architecture was later modified by Carl Gassner into the zinc-
carbon dry cell, replacing the liquid solution with an immobilizing paste that prevented spills
and enabled mass-market portable electronics.
Sources
1. Leclanche battery - Simple English Wikipedia, the free encyclopedia
2. leclanche cell meaning - English dictionary | VDict
User prompt: What did Plante make the “protective box” of when he demonstrated his battery with 9
cells in parallel
Response: When Gaston Planté presented his famous 9-cell secondary battery arrangement to the
French Academy of Sciences in 1860, the protective box housing the elements was made of tarred
pitch-pine (pitch-pin goudronné).
The interior of this wooden box was divided to hold the glass or hard rubber vessels containing the
spiral lead elements, and the wood was heavily treated with pitch (tar) to protect it from being
degraded by sulfuric acid splashes and leaks.
Sources
1. Philippe B. de l'Arc - Histoire de la voiture electrique - Philippe Boursin
User prompt: I read that an improved version of the Plante cell coated the plates with lead oxide.
Doesn’t that form on the lead plate automatically when charging?
Response: Yes, lead dioxide forms automatically on the positive plate when charging, but the
shortcut you are thinking of—manually coating the plates with lead oxide before assembly—was
the breakthrough invention introduced by Camille Alphonse Faure in 1881, over two decades
after Planté’s original design.
Planté's Original Method ("Forming"): Planté started with plain, smooth sheets of rolled
lead. When you first charge a plain lead cell, only the microscopic outermost skin of the metal
turns into lead dioxide ( ), yielding a very low electrical capacity. To make it useful,
Planté had to put the battery through a long, tedious "forming" process—repeatedly charging
it, discharging it, reversing the current, and letting it rest over weeks or months. This slow
electrochemical corrosion ate deeper into the lead, slowly building up a thin, deeply textured
layer of active lead oxides and dramatically increasing the surface area.
Faure’s Paste Method: Faure realized he could completely bypass months of tedious
electrochemical "forming" by physically pasting a layer of lead oxides (red lead and litharge
mixed with sulfuric acid) directly onto a cast lead grid. When first charged, that pre-existing
paste instantly converted into active sponge lead and lead dioxide, yielding a battery with
massive capacity right out of the gate and making mass-production commercially viable.
Sources
1. Lead–acid battery - Wikipedia
PbO  
2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 84/92
2. How Lead Acid Battery Grids Are Made Step by Step
User prompt: I saw a diagram of a pair of needles mounted vertically so that the points point
towards each other and a spark formed when connected to a battery.
Response: That configuration is a classic needle spark gap designed to demonstrate or utilize
concentrated electrical discharge.
The Physics of Sharp Points: Sharp points concentrate electric field lines intensely because
of their tiny radius of curvature. This high field gradient drastically lowers the threshold voltage
needed to ionize the surrounding air molecules, allowing a spark to bridge the gap much more
easily than it would between flat or rounded terminals.
The Voltaic Pile Context: While a low-voltage battery cannot jump an air gap on its own, a
large historical voltaic pile consisting of 50 to 100 or more series-connected plates generates
enough cumulative electromotive force to spark across a tiny gap when the circuit is
manipulated.
Make-and-Break Inductive Kicks: In many 19th-century illustrations, bringing pointed
conductors connected to a battery close together (or snapping them apart) demonstrated the
bright spark caused by self-induction—the sudden high-voltage spike created by the
collapsing magnetic field in the circuit wires when the current is interrupted.
User prompt: Hmm, so if the needles are connected there is a current flowing from the battery.
When the connection is broken the magnetic field created by the current collapses. That creates
the high voltage for a spark?
Response: The exact physical mechanism is self-induction, often referred to as an "inductive
kick" or flyback voltage.
Magnetic Energy Storage: Any circuit containing wire loops or coils possesses inductance (
). When a closed circuit allows current ( ) to flow from a battery, it builds up a surrounding
magnetic field that stores energy ( ).
The Rate of Current Change ( ): When you abruptly snap the connection apart, the time it
takes for the current to drop to zero is vanishingly small. This creates a massive, negative rate
of change in current ( ).
Faraday's Law of Induction: According to electromagnetic induction, the voltage generated
across an inductor is proportional to the rate of change of current:
Because  is so enormous during a sudden break, the induced voltage  spikes well above
the original battery voltage—sometimes reaching hundreds or thousands of volts.
L I
 LI2
1 2
 
dt
di
 
dt
di
V = −L  
dt
di
 
dt
di V
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 85/92
Overcoming Air Breakdown: That sudden voltage spike forces electrons to bridge the tiny
air gap between the sharp needle points, ionizing the air molecules and creating a brief, bright
spark before the magnetic field completely collapses.
User prompt: How does it work going the other way? Have to close it quickly enough to make Di/dt
large?
Response: When you close a circuit containing inductance, the electrical dynamics behave in the
exact opposite way, governed by the growth of current rather than its collapse.
The Back-EMF Barrier: When you push the needles together to close the circuit, current
attempts to jump from zero to its maximum value. Because an inductor resists any change in
current, it instantly generates a back-EMF (an induced voltage pointing in the opposite
direction of the battery) to fight that increase:
Delayed Current Rise: While the initial mathematical rate of change ( ) is steep the
moment contact is established, the resulting induced voltage acts against the battery source.
Instead of creating a massive voltage spike, it chokes and smooths out the incoming current,
forcing it to ramp up gradually according to the circuit's time constant ( ).
Pre-Contact Arcing: If you notice a tiny spark the instant you close a pair of needles, it is
generally not an inductive kick. Instead, it is a microscopic electrostatic pre-discharge—the
high electric field ionizes the air gap a split second before the metal actually touches.
The premise that closing a circuit quickly creates a large  inductive spike is incorrect. The
massive, high-energy voltage spike and bright spark occur exclusively when breaking the circuit,
because the collapsing magnetic field has nowhere else to force its energy except across the
opening air gap.
User prompt: How did people set up the circuit to have a high inductance?
Response: Nineteenth-century experimenters maximized circuit inductance by combining multi-turn
coil geometry, high-permeability cores, and specialized winding configurations:
Densely Wound Solenoids (Helixes): Because inductance scales with the square of the
number of turns ( ), builders like Joseph Henry and Charles Grafton Page wound
thousands of feet of insulated copper wire into tight, multi-layered cylindrical bobbins to
concentrate the magnetic field.
Bundled Iron Cores: Inserting a metal core dramatically increases inductance by
concentrating magnetic flux, but a solid iron bar suffers from severe energy losses due to
internal circulating currents (eddy currents). Experimenters solved this by stuffing the core
with a bundle of parallel, insulated soft-iron wires, which preserved high magnetic
permeability while blocking parasitic electrical currents.
V = −L  
dt
di
 
dt
di
τ =
 
R
L
 
dt
di
N 2
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 86/92
Coaxial Primary and Secondary Layers: Pioneers like Nicholas Callan and Heinrich
Ruhmkorff nested coils together. They used a short, thick primary wire connected to the
battery to generate a massive magnetic flux, surrounded by an insulated secondary winding
made of miles of ultra-thin wire to maximize the inductive coupling and voltage transformation.
Sources
1. Induction Coil - Physics - Kenyon College
User prompt: The diagram I see just had loosely coiled or spiral wires. Would that be enough to
create inductance?
Response: Any conductor carrying electric current possesses some degree of self-inductance, but
changing its geometry into a loop or a spiral dramatically amplifies that effect.
Magnetic Field Reinforcement: When a wire is straight, its magnetic field lines disperse
widely into space. Bending that same wire into a loose coil or spiral forces the magnetic field
lines from adjacent turns to overlap and reinforce one another, effectively concentrating the
magnetic flux within and around the coil.
The Turn-Count Scaling: Inductance scales with the square of the number of turns ( ) and
is proportional to the area enclosed by the loop. Even a loosely wound spiral or a helix with
just a few dozen turns stores substantially more magnetic energy than a straight wire of
identical length.
Historical Effectiveness: Early 19th-century experimenters routinely used simple, hand-
wound copper spirals or loose bobbins connected to a multi-cell voltaic battery. When the
circuit was abruptly broken, the magnetic energy stored even in a modest, loose coil was
more than sufficient to produce a sharp, bright inductive spark across a contact gap.
User prompt: Are the electrodes in a modern lead acid battery made of sponge lead and lead
dioxide?
Response: The negative electrode of a modern lead-acid battery consists of porous metallic lead,
commonly referred to as sponge lead, while the positive electrode is made of lead dioxide (
).
Both active materials are pasted onto cast lead-alloy grids to provide mechanical support and
current collection, and they are submerged in an electrolyte solution of dilute sulfuric acid ( ).
During discharge, both electrodes react with the sulfuric acid to form lead sulfate ( ), and
during charging, the reverse reaction converts them back into sponge lead and lead dioxide.
User prompt: The lead sulfate is in solution? And plates back into metal during charging?
N 2
PbO  
2
H  SO  
2 4
PbSO
 
4
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 87/92
Response: Lead sulfate is not dissolved in the liquid electrolyte. Because it has an extremely low
solubility in sulfuric acid, it precipitates out as a solid, fine-grained white crystalline deposit that
clings directly to and fills the porous interior of both electrode plates.
During the charging cycle, this solid layer does not behave like a standard metal-plating bath where
dissolved ions travel through a liquid and plate onto a cathode. Instead, it undergoes a solid-state
electrochemical conversion:
The Negative Plate: Solid lead sulfate is reduced directly back into porous metallic sponge
lead, releasing sulfate ions back into the surrounding liquid.
The Positive Plate: Solid lead sulfate is simultaneously oxidized into solid lead dioxide, also
returning sulfate ions to the electrolyte and restoring the strength of the sulfuric acid.
The premise that lead sulfate floats freely in solution and plates back into metal is incorrect. It
remains a solid mineral deposit on the plates that chemically transforms back into active electrode
material during charging.
User prompt: Ah, so that’s why lead acid cells don’t cope with deep discharge? What is different in
a deep cycle battery?
Response:
Plate Thickness and Surface Area: Starting (SLI) batteries use a high count of thin, highly
porous plates to maximize surface area for the massive, instantaneous current required to
crank an engine. Deep-cycle batteries swap this architecture for fewer, much thicker, heavier
plates, trading away high immediate cranking power for structural endurance.
Volume Expansion and Mechanical Stress: When lead and lead dioxide convert into lead
sulfate during discharge, the material expands significantly in volume. In a starting battery,
this heavy volume shift physically strains, warps, and shreds the delicate thin plates, causing
the active material to flake off ("shed") and drop uselessly to the bottom of the case. Thick
plates in deep-cycle batteries absorb this mechanical stress without fracturing.
Hard Sulfation Prevention: Deep discharges leave behind massive amounts of lead sulfate.
If allowed to sit on thin, fragile plates, those tiny crystals grow into large, stubborn, electrically
insulating crystals ("hard sulfation") that refuse to convert back during charging. Deep-cycle
batteries utilize denser active pastes, heavier grid alloys, and often glass-mat (AGM) or gel
containment to inhibit this destructive crystal growth, allowing them to safely cycle down to
50% or 80% capacity repeatedly.
Sources
1. Deep Cycle vs Starting vs Dual Purpose Batteries - Midtronics
2. [Full Guide] Starting Battery vs. Deep-Cycle Battery - LiTime
3. Deep Cycle vs Starting Battery: Which Is Right for You?
User prompt: Were the spark gaps spring loaded or how did they break the gap quickly?
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 88/92
Response: Early 19th-century experimenters used a mix of clever manual techniques and early
electromechanical devices to break circuits fast enough to generate sharp inductive sparks.
The File-and-Wire Method: Michael Faraday famously used a simple metal file connected to
one battery terminal while drawing a wire across its textured surface. The wire skipped rapidly
over the teeth, creating hundreds of microscopic, high-speed breaks a second that produced
a continuous, hissing stream of bright inductive sparks.
Spring-Loaded Automatic Interrupters (Neef’s Hammer): Invented in the 1830s by
Christian Ernst Neef, this became the standard mechanism for continuous induction coils. A
spring-steel armature holding a contact point was pulled toward the iron core by its magnetic
field the moment the circuit closed. That physical movement broke the contact, killing the
magnetic field, which caused a spring to instantly snap the contact back closed to restart the
cycle.
Spring-Loaded Hand Keys: For single, deliberate electrostatic or inductive "kicks," builders
used spring-loaded brass lever switches and telegraph-style keys. The tensioned spring
forced the contacts apart much faster than human fingers could pull them, ensuring a steep,
clean  voltage spike.
Verification: You can verify a clean, high-speed break by watching for a sharp, crisp snap and a
bright, localized point-source spark rather than a dull, lingering orange arc that drags out the
transition time.
What kind of circuit break mechanism are you planning to incorporate into your historical build?
User prompt: In this circuit diagram there is a “condenser” - in this likely 2 brass discs separated by
resin ? Or something else and what is the purpose in the induction circuit?
Response:
What it’s actually made of: Unlike Volta's electrostatic condensers (which sometimes used
brass discs and resin), the condenser in a historical induction coil is an early parallel-plate
capacitor constructed from alternating sheets of tinfoil interleaved with paraffin-waxed
paper, oiled silk, or mica. They were often stacked flat inside the base of the coil box or
rolled up tightly.
Preventing Contact Arcing: When the automatic interrupter (Neef's hammer) snaps open,
the massive inductive "kick" tries to maintain the current by forcing a spark to jump across the
opening contact points. This lingering arc would slowly burn away the platinum points and
bleed off energy. The condenser provides an immediate local storage reservoir, absorbing
that initial surge so the contacts open cleanly and instantly.
Sharpening the Rate of Collapse ( ): By absorbing the breaking current instantly, the
condenser forces the primary current to drop to zero in a fraction of a millisecond. This
creates an extreme  value, which maximizes the primary voltage spike and drastically
increases the secondary induced voltage transferred to the output spark gap.
Resonant LC Ringing: Once the condenser absorbs the charge, it momentarily bounces the
energy back into the primary coil in a brief, high-frequency oscillatory ring (forming an LC tank
 
dt
di
 
dt
di
 
dt
di
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 89/92
circuit with the primary winding). This rapid collapse and reversal of the magnetic field
accelerates the induction process before the spring pulls the contacts fully back together.
User prompt: In the neef’s hammer device the spark gap is connected to the secondary coil. Is that
to amplify the voltage from the induction spike?
Response: Yes, the spark gap is connected to the secondary coil precisely to harness a massive,
transformed voltage spike via mutual induction.
Turns Ratio Transformation: While the primary circuit handles the low-voltage battery power
and the high-current breaking spike, the secondary winding consists of thousands of turns of
fine insulated wire. According to the transformer turns ratio ( ), that
enormous primary voltage spike is multiplied by the massive ratio of secondary-to-primary
turns.
Stepping Up to Kilovolts: Even though the primary inductive kick might only reach a few
hundred volts, stepping that up through thousands of secondary turns pushes the potential to
tens or hundreds of thousands of volts.
Bridging the Gap: This extreme secondary voltage is what allows the spark to violently
ionize the air and jump across a wide external spark gap, turning a low-voltage DC current
into a high-voltage, high-frequency discharge.
User prompt: Do the turns in the secondary have to be in a single layer?
Response: No, the secondary winding in a classic induction coil is deliberately wound in multiple
layers rather than a single layer.
Achieving Massive Turns Ratios: To step a low battery voltage up to tens or hundreds of
thousands of volts, the secondary requires thousands—and sometimes miles—of fine wire
turns, which would be physically impossible to fit in a single layer along a core.
The High-Voltage Breakdown Risk: Stacking multiple layers introduces a severe design
challenge because high voltages accumulate rapidly between adjacent layers. If a wire
carrying thousands of volts ends up lying directly against a wire from a lower layer, the
extreme potential difference will cause a spark to punch right through the enamel insulation
and ruin the coil.
Sectional Winding Solutions: To prevent internal short circuits, historical coil builders like
Heinrich Ruhmkorff divided the secondary spool into dozens of isolated, thin compartments or
disk-like sections. This kept the cumulative voltage difference between adjacent wire turns low
enough that paraffin-wax or resin insulation could safely contain it.
User prompt: What about modern enameled wire?
V  =sec V  ×pri
 
N  
pri
N  
sec
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 90/92
Response: Modern magnet wire completely transforms the construction of induction coils by
replacing bulky historical insulations with high-performance synthetic polymer coatings.
Ultra-Thin Dielectric Layers: Modern enamels (such as modified polyurethane, polyester, or
polyimide) are applied as microscopic films that offer immense dielectric breakdown strength
—often several thousand volts per mil—drastically outperforming old silk, cotton, or paper
wraps.
Higher Fill Factor: Because the polymer coating takes up virtually zero physical space
compared to textile wrappings, you can pack significantly more copper turns into the same
volume, yielding a much higher magnetic field and turns ratio.
Thermal Resilience: Modern magnet wire is rated for high thermal classes (ranging from
Class B 130°C up to Class H 200°C or higher for polyimide/Kapton coats), meaning it can
handle internal heat from high currents without the insulation scorching, melting, or degrading.
Simplified Construction: It eliminates the messy historical requirement to hand-impregnate
every single layer with melted shellac, pitch, or paraffin wax during winding, though
interleaving a thin modern plastic film (like Mylar or capacitor film) between deep secondary
layers is still wise for extreme high-voltage builds to stop edge-to-edge tracking.
User prompt: Ehat tools did faraday use for n his experiments?
Response: Michael Faraday relied on a mix of standard 19th-century laboratory apparatus,
chemical batteries, and remarkably humble everyday materials to build his breakthrough devices:
Voltaic Cells and Batteries: He used early chemical batteries (like the voltaic piles and
trough configurations given to him by Alessandro Volta and developed by Humphry Davy) to
supply steady DC currents for his electromagnetic experiments.
Mercury Baths: For his early work on electromagnetic rotation (the first primitive electric
motor), he used glass vessels partially filled with liquid mercury to act as a fluid, continuous
electrical conductor.
Improvised Wire and Insulation: When constructing his famous 1831 induction ring (the first
transformer), he famously wound coils using ordinary copper wire intended for ladies'
bonnets, insulating the turns by hand with strips of cotton cloth.
Iron Rings and Soft-Iron Cores: He wound coils around specially forged soft-iron rings and
bar magnets to concentrate magnetic flux and study how magnetic fields interact with electric
circuits.
Galvanometers: To detect and measure the tiny, fleeting electric currents produced by
induction, he utilized sensitive early galvanometers—compass needles wrapped in multi-turn
wire coils.
Heavy Electromagnets and Optical Glass: In his later research on diamagnetism and the
magneto-optical effect, he employed a massive custom iron-core electromagnet powered by
large battery banks, alongside blocks of heavy, highly dense optical glass that he had
formulated himself years earlier.
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 91/92
9/10/26, 5:54 PM historical trough batttery
https://gemini.google.com/app/cd502d816727a98f 92/92