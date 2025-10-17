
# Gravity Slingshot Simulation

A simple gravity slingshot simulator built using Python and Pygame.  
This project visualizes how gravity from a massive stationary planet affects the motion of a moving object (like a spacecraft).

---

WHAT DOES IT DO : 
- One stationary planet with configurable mass  
- Object/spacecraft that can be placed anywhere using your mouse  
- Real-time gravitational force calculation between the planet and the object  
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
