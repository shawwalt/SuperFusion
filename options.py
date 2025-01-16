import argparse

class TrainOptions():
  def __init__(self):
    self.parser = argparse.ArgumentParser()

    # data loader related
    self.parser.add_argument('--dataroot', type=str, default='dataset/MSRS/train', help='path of data')
    self.parser.add_argument('--phase', type=str, default='train', help='phase for dataloading')
    self.parser.add_argument('--batch_size', type=int, default=12, help='batch size')
    self.parser.add_argument('--nThreads', type=int, default=8, help='# of threads for data loader')
    
    # ouptput related
    freq = 50
    self.parser.add_argument('--name', type=str, default='RF_MSRS', help='folder name to save outputs')
    self.parser.add_argument('--display_dir', type=str, default='./logs', help='path for saving display results')
    self.parser.add_argument('--result_dir', type=str, default='./results', help='path for saving result images and models')
    self.parser.add_argument('--display_freq', type=int, default=freq, help='freq (iteration) of display')
    self.parser.add_argument('--img_save_freq', type=int, default=freq, help='freq (epoch) of saving images')
    self.parser.add_argument('--model_save_freq', type=int, default=freq, help='freq (epoch) of saving models')
    self.parser.add_argument('--no_display_img', action='store_true', help='specified if no dispaly')

    # training related
    self.parser.add_argument('--lr_policy', type=str, default='lambda', help='type of learn rate decay')
    self.parser.add_argument('--n_ep', type=int, default=1200, help='number of epochs') # 400 * d_iter
    self.parser.add_argument('--n_ep_decay', type=int, default=600, help='epoch start decay learning rate, set -1 if no decay') # 200 * d_iter
    # self.parser.add_argument('--resume', type=str, default='./checkpoint/MSRS.pth', help='specified the dir of saved models for resume the training')
    self.parser.add_argument('--resume', type=str, default=None, help='specified the dir of saved models for resume the training')
    self.parser.add_argument('--gpu', type=int, default=0, help='gpu')
    self.parser.add_argument('--stage', type=str, default='RF', help='reg&fus (RF) or fus&seg (FS)')
    
    #segmentation related
    # self.parser.add_argument('--dataroot_val', type=str, default='./dataset/MSRS/test', help="data for segmentation validation")
  def parse(self):
    self.opt = self.parser.parse_args()
    args = vars(self.opt)
    print('\n--- load options ---')
    for name, value in sorted(args.items()):
      print('%s: %s' % (str(name), str(value)))
    return self.opt
