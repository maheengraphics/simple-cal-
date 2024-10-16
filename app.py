import streamlit as st

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Streamlit app
def calculator():
    st.title("Simple Calculator")

    # Dropdown menu for selecting operation
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Input fields for numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Button to perform the calculation
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        # Display the result
        st.success(f"The result is: {result}")

# Run the calculator app
if __name__ == "__main__":
    calculator()
