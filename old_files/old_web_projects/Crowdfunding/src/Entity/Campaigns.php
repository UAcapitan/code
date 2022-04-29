<?php

namespace App\Entity;

use App\Repository\CampaignsRepository;
use Doctrine\Common\Collections\ArrayCollection;
use Doctrine\Common\Collections\Collection;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass=CampaignsRepository::class)
 */
class Campaigns
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=100)
     */
    private $name;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $description;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $video;

    /**
     * @ORM\Column(type="integer")
     */
    private $money;

    /**
     * @ORM\Column(type="date")
     */
    private $date;

    /**
     * @ORM\ManyToOne(targetEntity=User::class, inversedBy="campaigns")
     * @ORM\JoinColumn(nullable=false)
     */
    private $user;

    /**
     * @ORM\OneToMany(targetEntity=Tags::class, mappedBy="campaigns")
     */
    private $tags;

    /**
     * @ORM\OneToMany(targetEntity=Image::class, mappedBy="campaigns", orphanRemoval=true)
     */
    private $images;

    /**
     * @ORM\Column(type="string", length=50)
     */
    private $subject;

    /**
     * @ORM\OneToMany(targetEntity=Bonuses::class, mappedBy="campaign", orphanRemoval=true)
     */
    private $bonuses;

    /**
     * @ORM\Column(type="integer")
     */
    private $now_money;

    /**
     * @ORM\OneToMany(targetEntity=BonusesUser::class, mappedBy="campaign", orphanRemoval=true)
     */
    private $bonusesUsers;

    /**
     * @ORM\OneToMany(targetEntity=Comments::class, mappedBy="campaign", orphanRemoval=true)
     */
    private $comments;

    /**
     * @ORM\OneToMany(targetEntity=Ratings::class, mappedBy="campaigns", orphanRemoval=true)
     */
    private $ratings;

    /**
     * @ORM\OneToMany(targetEntity=News::class, mappedBy="campaigns", orphanRemoval=true)
     */
    private $news;

    public function __construct()
    {
        $this->tags = new ArrayCollection();
        $this->images = new ArrayCollection();
        $this->bonuses = new ArrayCollection();
        $this->bonusesUsers = new ArrayCollection();
        $this->comments = new ArrayCollection();
        $this->ratings = new ArrayCollection();
        $this->news = new ArrayCollection();
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getName(): ?string
    {
        return $this->name;
    }

    public function setName(string $name): self
    {
        $this->name = $name;

        return $this;
    }

    public function getDescription(): ?string
    {
        return $this->description;
    }

    public function setDescription(string $description): self
    {
        $this->description = $description;

        return $this;
    }

    public function getVideo(): ?string
    {
        return $this->video;
    }

    public function setVideo(string $video): self
    {
        $this->video = $video;

        return $this;
    }

    public function getMoney(): ?int
    {
        return $this->money;
    }

    public function setMoney(int $money): self
    {
        $this->money = $money;

        return $this;
    }

    public function getDate(): ?\DateTimeInterface
    {
        return $this->date;
    }

    public function setDate(\DateTimeInterface $date): self
    {
        $this->date = $date;

        return $this;
    }

    public function getUser(): ?User
    {
        return $this->user;
    }

    public function setUser(?User $user): self
    {
        $this->user = $user;

        return $this;
    }

    /**
     * @return Collection|Tags[]
     */
    public function getTags(): Collection
    {
        return $this->tags;
    }

    public function addTag(Tags $tag): self
    {
        if (!$this->tags->contains($tag)) {
            $this->tags[] = $tag;
            $tag->setCampaigns($this);
        }

        return $this;
    }

    public function removeTag(Tags $tag): self
    {
        if ($this->tags->removeElement($tag)) {
            // set the owning side to null (unless already changed)
            if ($tag->getCampaigns() === $this) {
                $tag->setCampaigns(null);
            }
        }

        return $this;
    }

    /**
     * @return Collection|Image[]
     */
    public function getImages(): Collection
    {
        return $this->images;
    }

    public function addImage(Image $image): self
    {
        if (!$this->images->contains($image)) {
            $this->images[] = $image;
            $image->setCampaigns($this);
        }

        return $this;
    }

    public function removeImage(Image $image): self
    {
        if ($this->images->removeElement($image)) {
            // set the owning side to null (unless already changed)
            if ($image->getCampaigns() === $this) {
                $image->setCampaigns(null);
            }
        }

        return $this;
    }

    public function getSubject(): ?string
    {
        return $this->subject;
    }

    public function setSubject(string $subject): self
    {
        $this->subject = $subject;

        return $this;
    }

    /**
     * @return Collection|Bonuses[]
     */
    public function getBonuses(): Collection
    {
        return $this->bonuses;
    }

    public function addBonus(Bonuses $bonus): self
    {
        if (!$this->bonuses->contains($bonus)) {
            $this->bonuses[] = $bonus;
            $bonus->setCampaign($this);
        }

        return $this;
    }

    public function removeBonus(Bonuses $bonus): self
    {
        if ($this->bonuses->removeElement($bonus)) {
            // set the owning side to null (unless already changed)
            if ($bonus->getCampaign() === $this) {
                $bonus->setCampaign(null);
            }
        }

        return $this;
    }

    public function getNowMoney(): ?int
    {
        return $this->now_money;
    }

    public function setNowMoney(int $now_money): self
    {
        $this->now_money = $now_money;

        return $this;
    }

    /**
     * @return Collection|BonusesUser[]
     */
    public function getBonusesUsers(): Collection
    {
        return $this->bonusesUsers;
    }

    public function addBonusesUser(BonusesUser $bonusesUser): self
    {
        if (!$this->bonusesUsers->contains($bonusesUser)) {
            $this->bonusesUsers[] = $bonusesUser;
            $bonusesUser->setCampaign($this);
        }

        return $this;
    }

    public function removeBonusesUser(BonusesUser $bonusesUser): self
    {
        if ($this->bonusesUsers->removeElement($bonusesUser)) {
            // set the owning side to null (unless already changed)
            if ($bonusesUser->getCampaign() === $this) {
                $bonusesUser->setCampaign(null);
            }
        }

        return $this;
    }

    /**
     * @return Collection|Comments[]
     */
    public function getComments(): Collection
    {
        return $this->comments;
    }

    public function addComment(Comments $comment): self
    {
        if (!$this->comments->contains($comment)) {
            $this->comments[] = $comment;
            $comment->setCampaign($this);
        }

        return $this;
    }

    public function removeComment(Comments $comment): self
    {
        if ($this->comments->removeElement($comment)) {
            // set the owning side to null (unless already changed)
            if ($comment->getCampaign() === $this) {
                $comment->setCampaign(null);
            }
        }

        return $this;
    }

    /**
     * @return Collection|Ratings[]
     */
    public function getRatings(): Collection
    {
        return $this->ratings;
    }

    public function addRating(Ratings $rating): self
    {
        if (!$this->ratings->contains($rating)) {
            $this->ratings[] = $rating;
            $rating->setCampaigns($this);
        }

        return $this;
    }

    public function removeRating(Ratings $rating): self
    {
        if ($this->ratings->removeElement($rating)) {
            // set the owning side to null (unless already changed)
            if ($rating->getCampaigns() === $this) {
                $rating->setCampaigns(null);
            }
        }

        return $this;
    }

    /**
     * @return Collection|News[]
     */
    public function getNews(): Collection
    {
        return $this->news;
    }

    public function addNews(News $news): self
    {
        if (!$this->news->contains($news)) {
            $this->news[] = $news;
            $news->setCampaigns($this);
        }

        return $this;
    }

    public function removeNews(News $news): self
    {
        if ($this->news->removeElement($news)) {
            // set the owning side to null (unless already changed)
            if ($news->getCampaigns() === $this) {
                $news->setCampaigns(null);
            }
        }

        return $this;
    }
}
