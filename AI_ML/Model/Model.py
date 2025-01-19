import tensorflow as tf
import numpy as np
import random
from collections import deque
from Controller.Controller import Controller

global epsilon
state_size = 6 
action_size = 4  
learning_rate = 0.001
gamma = 0.99
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01
batch_size = 64
memory_size = 2000
episodes = 1000
target_update_freq = 10


memory = deque(maxlen=memory_size)


def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, input_dim=state_size, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(action_size, activation='linear')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate),
                  loss='mse')
    return model


main_model = build_model()
target_model = build_model()
target_model.set_weights(main_model.get_weights())


def get_action(state):
    if np.random.rand() <= epsilon:
        return random.randint(0, action_size - 1)
    q_values = main_model.predict(state[np.newaxis], verbose=0)
    return np.argmax(q_values[0])  


def train_model():
    if len(memory) < batch_size:
        return
    
    minibatch = random.sample(memory, batch_size)
    states, actions, rewards, next_states, dones = zip(*minibatch)

    states = np.array(states)
    next_states = np.array(next_states)
    targets = main_model.predict(states, verbose=0)
    target_next = target_model.predict(next_states, verbose=0)
    
    for i in range(batch_size):
        if dones[i]:
            targets[i, actions[i]] = rewards[i]
        else:
            targets[i, actions[i]] = rewards[i] + gamma * np.max(target_next[i])

    main_model.fit(states, targets, epochs=1, verbose=0, batch_size=batch_size)


for episode in range(episodes):
    state = Controller.resetGameState()
    total_reward = 0
    
    while True:
        action = get_action(state)
        next_state, reward, done, _ = Controller.step(action)
        memory.append((state, action, reward, next_state, done))
        state = next_state
        total_reward += reward
        
        train_model()
        
        if done:
            print(f"Episode: {episode}, Total Reward: {total_reward}")
            break
    

    epsilon = max(epsilon_min, epsilon * epsilon_decay)
    

    if episode % target_update_freq == 0:
        target_model.set_weights(main_model.get_weights())


main_model.save_weights("tetris_dqn_weights.h5")
