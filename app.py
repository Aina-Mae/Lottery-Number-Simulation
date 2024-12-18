import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit App UI
st.title('Lottery Number Simulation')
st.write("This app generates a new set of random lottery numbers every time you select a lottery type.")

# Select lottery type
lottery_type = st.selectbox(
    'Select Lottery Type',
    ['6/42 Lotto', '6/49 Super Lotto', '6/55 Grand Lotto', '6/58 Ultra Lotto']
)

# Set number of lottery numbers and max number based on selected lottery type
if lottery_type == '6/42 Lotto':
    NUMBERS_PER_DRAW = 6
    MAX_NUMBER = 42
elif lottery_type == '6/49 Super Lotto':
    NUMBERS_PER_DRAW = 6
    MAX_NUMBER = 49
elif lottery_type == '6/55 Grand Lotto':
    NUMBERS_PER_DRAW = 6
    MAX_NUMBER = 55
else:  # '6/58 Ultra Lotto'
    NUMBERS_PER_DRAW = 6
    MAX_NUMBER = 58

# Button to generate random numbers
if st.button("Generate Random Numbers"):
    # Generate 6 random lottery numbers for a single draw
    np.random.seed()  # Random seed based on system time, ensuring new numbers each time
    lottery_numbers = np.random.choice(range(1, MAX_NUMBER + 1), size=NUMBERS_PER_DRAW, replace=False)

    # Display the generated lottery numbers
    st.subheader(f"Generated {lottery_type} Numbers")
    st.write(f"Your randomly selected numbers are: {sorted(lottery_numbers)}")

    # Optionally, visualize the numbers in a simple bar chart
    st.subheader(f"{lottery_type} - Frequency Chart of Selected Numbers")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(sorted(lottery_numbers), [1] * len(lottery_numbers), color='skyblue', edgecolor='black')
    ax.set_title('Frequency of Selected Lottery Numbers', fontsize=16)
    ax.set_xlabel('Lottery Number', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    st.pyplot(fig)

# Conclusion
st.write("""
### Conclusion:
- The app generates a new set of random lottery numbers every time you click the "Generate Random Numbers" button.
- You can observe how the lottery numbers are randomly selected based on the lottery type you choose.
""")
