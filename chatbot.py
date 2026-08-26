import streamlit as st

st.title("Traffic Assistant Chatbot 🤖")
st.write("Ask me anything about traffic rules, road signs, and driving regulations!")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def get_traffic_response(query):
    query = query.lower()
    if "red light" in query:
        return "A red traffic light means you must come to a complete stop before the intersection or stop line and wait until the light turns green."
    elif "speed limit" in query:
        return "Speed limits vary by zone. Generally, urban areas limit speeds to 40-50 km/h, while highways allow 80-100 km/h. Always follow posted road signs."
    elif "helmet" in query:
        return "Yes, wearing a certified helmet is legally mandatory for both the driver and the pillion rider on a motorcycle."
    elif "stop sign" in query:
        return "A octagonal red STOP sign means you must bring your vehicle to a complete halt, yield to pedestrians and oncoming traffic, and proceed only when safe."
    elif "parking" in query:
        return "Parking is prohibited near intersections, fire hydrants, pedestrian crossings, or in front of yellow curb lines."
    else:
        return "I can help answer questions regarding traffic lights, speed limits, road signs, helmet rules, and parking regulations. Try asking about one of those!"


if prompt := st.chat_input("Ask about traffic rules..."):
   
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    
    response = get_traffic_response(prompt)
    
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)