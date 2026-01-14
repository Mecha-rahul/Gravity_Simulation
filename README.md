
# Gravity Slingshot Simulation

A simple gravity slingshot simulator built using Python and Pygame.  
This project visualizes how gravity from a massive stationary planet affects the motion of a moving object (like a spacecraft).

---

# Gravitational simukation 3 objects(2 Planets and 1 obj/spacecraft)

its a bit more complex than the simple slingshto tho the only difference between from prev one is that , in this we will calculate the Net force , Net acceleration and lastly we will also use dt(to show respectivness in case of acc,veland dissplacement ). similar to previos, we hvae used pygame lib. from this project, we can see how gravity affects a object between 2 stationary planets .

---

# DEMO VIDEO OF BOTH
[![Watch The Video](https://img.youtube.com/vi/JlzO4pARLS0?si=qyMiDvRE8KGB9UQO/0.jpg)](https://youtu.be/JlzO4pARLS0?si=qyMiDvRE8KGB9UQO)


WHAT DOES IT DO : 
- One stationary planet with configurable mass(slingshot file)
- Two stationary planet with configurable mass(3 object file) 
- Object/spacecraft that can be placed anywhere using your mouse  
- Real-time gravitational force calculation between the planets and the object  
- Smooth motion simulation based on Newtonian physics  
- Displays planet mass, object speed, acceleration, and other parameters on-screen  
- Interactive setup — click to create new spacecraft and watch its orbit or slingshot path

---

PHYSICS AND LOGIC BEHIND :
so bsicaly used  newtons force between two masses equation , as both of my bodies have thier own mass , radius and one of them have a velocity vector so we can easily calculate the force and the angle using py game features and see the real time consequences .
Where:
- \( F \) = gravitational force  
- \( G \) = gravitational constant  
- \( m_1, m_2 \) = masses of the planet and object  
- \( d \) = distance between them  

The resulting acceleration influences the spacecraft’s velocity, creating orbital or slingshot trajectories depending on initial conditions.

---
# requirment 
python and pygame lib
pip install pygame

# Future updates
- some future updates, that i have in my mind is adding a trail behind object , adding glow and flare in planets , make simulation more attractive , for noe the code is very messy . 