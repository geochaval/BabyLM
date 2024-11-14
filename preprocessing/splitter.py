import os
import glob

input_directory = './pretrain/bnc'
train_file = './pretrain/train.txt'
validation_file = './pretrain/validation.txt'

train_word_limit = 1e7
valid_word_limit = 2e6
train_word_count = 0
valid_word_count = 0
writing_to_train = True 

with open(train_file, 'w', newline='\n', encoding="utf-8") as train_out, open(validation_file, 'w', newline='\n', encoding="utf-8") as valid_out:
        for part in glob.glob(f"{input_directory}/*/*/*.md"):
            file_path = part
            with open(file_path, 'r', encoding="utf-8") as infile:
                content = infile.read()
                filtered_content = [line for line in content.splitlines() if not line.lstrip().startswith('#')]

                # Join the filtered lines back into a single string
                content = '\n'.join(filtered_content)
                word_count = len(content.split())

                # Determine where to write: train or validation
                if writing_to_train:
                    if train_word_count + word_count <= train_word_limit:
                        train_out.write(content + '\n\n')
                        train_word_count += word_count
                    else:
                            # Write only up to the limit
                        print(train_word_count)
                        train_out.write(content + '\n\n')
                        train_word_count += word_count
                        writing_to_train = False  # Switch to validation file for remaining documents
                else:
                    if valid_word_count + word_count <= valid_word_limit:
                        valid_out.write(content + '\n\n')
                        valid_word_count += word_count
                    else:
                        # Write only up to the limit
                        print(valid_word_count)
                        valid_out.write(content + '\n\n')
                        valid_word_count += word_count
                        break  # Stop once validation limit is reached

print(f"Train file created with {train_word_count} words at {train_file}")
print(f"Validation file created with {valid_word_count} words at {validation_file}")