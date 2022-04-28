import tensorflow as tf

predictor = tf.saved_model.load('one_step')

states = None
next_char = tf.constant(['It’s the inside which comes out, '])
result = [next_char]

for n in range(2000):
  next_char, states = predictor.generate_one_step(next_char, states=states)
  result.append(next_char)

result = tf.strings.join(result)
print(result[0].numpy().decode('utf-8'), '\n\n' + '_'*80)
