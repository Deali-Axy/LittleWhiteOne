from core.trainers import ChatterBotCorpusTrainer
import bot

if __name__ == '__main__':
    trainer = ChatterBotCorpusTrainer(bot.little_white)
    # trainer.train("core.corpus.chinese")
    trainer.train("core.corpus.english")
    trainer.train("core.corpus.custom")


